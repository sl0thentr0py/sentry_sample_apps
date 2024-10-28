import opentelemetry
import sentry_sdk
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


sentry_sdk.init(
    debug=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    _experiments={"otel_powered_performance": True},
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
    count = User.query.count()
    expensive()
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
