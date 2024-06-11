import sentry_sdk
from opentelemetry import trace
from time import sleep

sentry_sdk.init(
    debug=True,
    traces_sample_rate=1.0,
    _experiments={"otel_powered_performance": True},
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("root"):
    with tracer.start_as_current_span("db"):
        sleep(0.5)
        with tracer.start_as_current_span("redis"):
            sleep(0.2)
    with tracer.start_as_current_span("http"):
        sleep(1)
