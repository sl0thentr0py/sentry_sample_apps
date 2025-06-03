import sentry_sdk
import time
import requests
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor


def traces_sampler(sampling_context):
    if "favicon" in sampling_context["url.path"]:
        return 0.0
    else:
        return 1.0

sentry_sdk.init(
    release=f"flask-sqlalchemy-{sentry_sdk.VERSION}",
    debug=True,
    traces_sample_rate=1.0,
    default_integrations=False,
)


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)


FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
SQLAlchemyInstrumentor().instrument(engine=db.engine)


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
        time.sleep(0.1)
        requests.get("http://localhost:3000/success")

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
