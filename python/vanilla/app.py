import time
import sentry_sdk
from opentelemetry import trace
from opentelemetry.propagate import set_global_textmap
from opentelemetry.trace import Status, StatusCode
from opentelemetry.sdk.trace import TracerProvider
from sentry_sdk.integrations.opentelemetry import SentrySpanProcessor, SentryPropagator

sentry_sdk.init(
    traces_sample_rate=1.0,
    debug=True,
    instrumenter="otel",
)

provider = TracerProvider()
provider.add_span_processor(SentrySpanProcessor())
trace.set_tracer_provider(provider)
set_global_textmap(SentryPropagator())
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("tx") as tx:
    status = Status(status_code=StatusCode.ERROR)
    tx.set_status(status)

    with tracer.start_as_current_span("span") as span:
        status = Status(status_code=StatusCode.ERROR)
        span.set_status(status)
        time.sleep(3)

sentry_sdk.flush()
