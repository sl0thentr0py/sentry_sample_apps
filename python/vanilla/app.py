import datetime
import sentry_sdk
from sentry_sdk.utils import format_timestamp


def before_send(event, hint):
    event["extra"] = { "started_at": None }
    return event


sentry_sdk.init(debug=True, traces_sample_rate=1.0, before_send=before_send)

1 / 0
