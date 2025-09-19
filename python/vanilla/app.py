from time import sleep
import sentry_sdk
from opentelemetry.trace import use_span, INVALID_SPAN

sentry_sdk.init(
    debug=True,
    traces_sample_rate=1.0,
)

with sentry_sdk.start_span(name="parent"):
    with sentry_sdk.start_span(name="child"):
        sleep(0.2)
    with use_span(INVALID_SPAN):
        with sentry_sdk.start_span(name="child2"):
            sleep(1)
            with sentry_sdk.start_span(name="child3"):
                sleep(0.5)


sentry_sdk.flush()
