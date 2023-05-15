import sentry_sdk
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


sentry_sdk.init(
    traces_sample_rate=1.0,
    # send_default_pii=True,
    # debug=True
)


app = Flask(__name__)
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


@app.route("/count")
def count():
    count = User.query.count()
    return f"<p>count: {count} </p>"


@app.route('/ds')
def get_tasks():
    return jsonify({'extenal': 42})


@app.route("/scrubber", methods=['POST'])
def test():
    raise Exception("bla")
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    # db.create_all() # uncomment for first time
    app.run()
