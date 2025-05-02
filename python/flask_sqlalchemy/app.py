import sentry_sdk
from sentry_sdk.transport import HttpTransport
import requests
import time
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


sentry_sdk.init(
    release=f"flask-sqlalchemy-{sentry_sdk.VERSION}",
    transport=FileWriteHttpTransport,
    debug=True,
    traces_sampler=traces_sampler,
    # profiles_sample_rate=0.1,
)


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)


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
def count():
    sentry_sdk.set_user({"email":"jane.doe@adas.com"})
    sentry_sdk.set_tag("foo", 42)
    sentry_sdk.set_tag("bar", "baz")
    count = User.query.count()

    with sentry_sdk.start_span(name="sleep") as span:
        span.set_data("span_foo", 23)
        time.sleep(1)
    # requests.get("http://localhost:3000/success")
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
    return 420.69 / 0


if __name__ == "__main__":
    # db.create_all() # uncomment for first time
    app.run()
