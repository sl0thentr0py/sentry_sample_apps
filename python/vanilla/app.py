import logging
import weakref
import time
import sentry_sdk

sentry_sdk.init()

weak_exception = None
class CustomException(Exception):
    pass

def callback(ref):
    print("Exception was garbage collected!")

try:
    raise CustomException('Custom Exception')
except Exception as e:
    logging.exception("Exception logging")
    weak_exception = weakref.ref(e, callback)
    sentry_sdk.flush()

while True:
    time.sleep(1)
    print(weak_exception())
