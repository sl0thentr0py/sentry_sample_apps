import sentry_sdk
from opentelemetry import trace
from time import sleep

sentry_sdk.init(
    debug=True,
    traces_sample_rate=1.0,
    _experiments={"otel_powered_performance": True},
)


sentry_sdk.set_tag("tag.global", 99)

## sentry apis
with sentry_sdk.start_span(description="sentry request"):
    sentry_sdk.set_tag("tag.inner", "asd")
    sleep(0.1)
    with sentry_sdk.start_span(description="sentry db"):
        sleep(0.5)
        with sentry_sdk.start_span(description="sentry redis"):
            sleep(0.2)
    with sentry_sdk.start_span(description="sentry http"):
        sleep(1)

## otel apis
# tracer = trace.get_tracer(__name__)

# with tracer.start_as_current_span("request"):
#     sleep(0.1)
#     with tracer.start_as_current_span("db"):
#         sleep(0.5)
#         with tracer.start_as_current_span("redis"):
#             sleep(0.2)
#     with tracer.start_as_current_span("http"):
#         sleep(1)
