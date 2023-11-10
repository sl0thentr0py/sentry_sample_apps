from time import sleep, time
import sentry_sdk
from sentry_sdk import push_scope, capture_message

import logging

log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

sentry_sdk.init()

def send():
    with push_scope() as scope:
        scope.add_attachment(bytes=b"Hello World! " * 200000, filename="attachment.txt")
        capture_message('Boo')

# # 15 min
# end = time() + 15 * 60

# while time() < end:
#     send()
#     sleep(0.1)

for i in range(10):
    send()

# sleep(15*60)

# for i in range(10):
#     send()

sentry_sdk.flush()
