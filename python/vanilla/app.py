import time
import sentry_sdk
from sentry_sdk import start_span, start_transaction


sentry_sdk.init(debug=True, traces_sample_rate=1.0)

with start_transaction(name="neel tx"):
    with start_span(op="neel op", description="neel's span") as span:
        span.set_tag("neel.boolean.tag", True)
        time.sleep(1)
