import sentry_sdk
from sentry_sdk.consts import SPANSTATUS

sentry_sdk.init(
    traces_sample_rate=1.0,
    debug=True,
)

with sentry_sdk.start_transaction(name="test"):
    with sentry_sdk.start_span(op="foo", description="bar") as span:
        span.set_status(SPANSTATUS.DEADLINE_EXCEEDED)

sentry_sdk.flush()
