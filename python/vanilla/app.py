import time
import sentry_sdk

sentry_sdk.init(
    debug=True,
    traces_sample_rate=1.0,
)

@sentry_sdk.trace(op="foo", name="tasd")
def foo():
    time.sleep(2)

foo()
