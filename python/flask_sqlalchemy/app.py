import pympler
import sentry_sdk
import opentelemetry
from sentry_sdk.transport import HttpTransport
import requests
import time
import linecache
import tracemalloc
import gc
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


class FileWriteHttpTransport(HttpTransport):
    def _serialize_envelope(self, envelope):
        release = self.options["release"]
        project_root = self.options["project_root"]

        from pathlib import Path
        path = Path(f"{project_root}/out/{release}")
        path.parent.mkdir(parents=True, exist_ok=True) 
        with open(path, "ab") as f:
            envelope.serialize_into(f)

        return super()._serialize_envelope(envelope)


def traces_sampler(sampling_context):
    if "favicon" in sampling_context["url.path"]:
        return 0.0
    else:
        return 1.0


def display_top(snapshot, key_type='lineno', limit=5):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(True, "*sentry_sdk/opentelemetry/span_processor*"),
        tracemalloc.Filter(True, "*opentelemetry*"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


sentry_sdk.init(
    release=f"flask-sqlalchemy-{sentry_sdk.VERSION}",
    # transport=FileWriteHttpTransport,
    debug=True,
    traces_sample_rate=1.0,
    # profiles_sample_rate=0.1,
)


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)
# tracemalloc.start()


def track_memory(func):
    def wrapper(*args, **kwargs):
        snapshot1 = tracemalloc.take_snapshot()
        display_top(snapshot1)

        result = func(*args, **kwargs)

        gc.collect()

        snapshot2 = tracemalloc.take_snapshot()
        display_top(snapshot2)
        # top_stats = snapshot2.compare_to(snapshot1, "lineno") 

        return result
    return wrapper


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=False, nullable=False)


@app.route("/insert")
def insert():
    db.session.add(User(username="Flask"))
    db.session.commit()
    return "<p>inserted!</p>"

def expensive():
    import math
    for _ in range(100000000):
        math.sqrt(64*64*64*64*64)

@app.route("/count")
# @track_memory
def count():
    sentry_sdk.set_user({"email":"jane.doe@adas.com"})
    sentry_sdk.set_tag("foo", 42)
    sentry_sdk.set_tag("bar", "baz")
    count = User.query.count()

    with sentry_sdk.start_span(name="sleep") as span:
        span.set_data("span_foo", 23)
        time.sleep(0.1)

    return f"<p>count: {count} </p>"


@app.route('/ds')
def get_tasks():
    return jsonify({'extenal': 42})


@app.route("/scrubber", methods=['POST'])
def test():
    raise Exception("bla")
    return "<p>Hello, World!</p>"


@app.route("/twp")
def twp():
    requests.get("http://localhost:3000/error")
    raise Exception("twp flask")


@app.route("/error")
def error():
    sentry_sdk.get_isolation_scope().add_attachment(bytes=b"hello attachemnt", filename="test.txt")
    return 420.69 / 0


if __name__ == "__main__":
    # db.create_all() # uncomment for first time
    app.run()
