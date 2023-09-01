import sentry_sdk
from celapp import app


@app.task
def task():
    print("wassup")
    sentry_sdk.capture_message('should report this message')
    raise Exception('should also report this exception')


@app.task()
def divide_by_zero():
    return 1 / 0


@app.task()
def try_dividing_by_zero():
    try:
        print("I wonder what 1 divided by zero is. Let's try it out...")
        divide_by_zero().delay()
    except ZeroDivisionError:
        print(
            "Don't be silly! Division by zero is undefined and causes an error in Python."
        )
        print("Fortunately, I was here to handle the error!")


if __name__ == "__main__":
    try_dividing_by_zero.delay()
