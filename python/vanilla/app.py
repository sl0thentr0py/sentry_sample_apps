import time
import sentry_sdk
from sentry_sdk.integrations.otlp import OTLPIntegration
from opentelemetry import trace

sentry_sdk.init(
    debug=True,
    integrations=[OTLPIntegration(capture_exceptions=True)],
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("tx") as tx:
    with tracer.start_as_current_span("span") as span:
        time.sleep(3)
    with tracer.start_as_current_span("error") as error_span:
        1 / 0

sentry_sdk.flush()
