import sentry_sdk
import requests
import time
from flask import Flask, jsonify, stream_with_context, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

import sentry_sdk
from sentry_sdk.integrations.otlp import OtlpIntegration

## need OTEL_EXPORTER_OTLP_TRACES_ENDPOINT and OTEL_EXPORTER_OTLP_TRACES_HEADERS in env
otlp_exporter = OTLPSpanExporter()
span_processor = BatchSpanProcessor(otlp_exporter)
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(span_processor)

sentry_sdk.init(
    debug=True,
    integrations=[OtlpIntegration()],
)

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

# Instrument Flask, Requests, and SQLAlchemy
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
SQLAlchemyInstrumentor().instrument(engine=db.engine)

tracer = trace.get_tracer(__name__)

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


@app.route("/scoped-response")
def myroute():
    @stream_with_context
    def generate():
        yield b"hello"
        sentry_sdk.set_tag("foo", "bar")
        yield b"world"
        1/0

    return Response(generate())


@app.route("/count")
def count():
    sentry_sdk.set_transaction_name("custom_scope_api")
    count = User.query.count()
    with tracer.start_as_current_span(name="sleep"):
        time.sleep(1)
    requests.get("https://example.com")
    with tracer.start_as_current_span(name="exception here"):
        try:
            1 / 0
        except:
            sentry_sdk.capture_exception()
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
