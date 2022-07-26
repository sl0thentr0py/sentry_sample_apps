import sentry_sdk
from celapp import app


@app.task
def task():
    print("wassup")
    sentry_sdk.capture_message('should report this message')
    raise Exception('should also report this exception')
