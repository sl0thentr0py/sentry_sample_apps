import threading
import urllib3

import sentry_sdk
from sentry_sdk.hub import Hub
from sentry_sdk.scope import add_global_event_processor


sentry_sdk.init(debug=True)


breadcrumbs = []
lock = threading.Lock()


@add_global_event_processor
def request_breadcrumb_processor(event, hint):
    global lock
    global breadcrumbs

    with lock:
        event["breadcrumbs"]["values"].extend(breadcrumbs)

    return event


def foo():
    global lock
    global breadcrumbs

    http = urllib3.PoolManager()
    http.request("GET", "https://httpbin.org/get")

    with lock:
        breadcrumbs.extend(Hub.current.scope._breadcrumbs)


def bar():
    sentry_sdk.capture_message("event with request")


x = threading.Thread(target=foo)
x.start()
x.join()
bar()
