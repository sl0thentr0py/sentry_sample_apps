import sentry_sdk
from threading import Thread
from time import sleep

sentry_sdk.init()

def work():
    for i in range(500):
        try:
            1 / 0
        except Exception:
            sentry_sdk.capture_exception()

def size():
    return sentry_sdk.Hub.current.client.transport._worker._queue.qsize()

def measure():
    while size() > 0:
        sleep(0.1)
        print(f"queue size {size()}")

t1 = Thread(target=work)
t2 = Thread(target=measure)

t1.run()
t2.run()

times = sentry_sdk.Hub.current.client.transport._worker._times
print(f"min: {min(times)}, mean: {sum(times) / len(times)}, max: {max(times)}")
