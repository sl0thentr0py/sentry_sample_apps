import datetime
import sentry_sdk
from sentry_sdk.utils import format_timestamp


def before_send(event, hint):
    event["request"] = { "headers": [["Foo", "Bar"]] }
    event["_meta"] = { "request": { "headers": { "0": { "1" : { "": { "rem": [["@password:filter","s",0,10]],"len":15}}}}}}

    return event


sentry_sdk.init(debug=True, traces_sample_rate=1.0, before_send=before_send)

1 / 0
