from time import sleep, time
import sentry_sdk


sentry_sdk.init(traces_sample_rate=1.0, _experiments={"enable_backpressure_handling": True})

def size():
    q = sentry_sdk.Hub.current.client.transport._worker._queue
    print(f"size: {q.qsize()}, full: {q.full()}")


last = time()
times = []

print("running heavy load")
for i in range(50):
    for j in range(1000):
        with sentry_sdk.start_transaction(name='backpressure'):
            for i in range(10):
                with sentry_sdk.start_span(op='sleep', description='zzz'):
                    pass
    now = time()
    times.append(now - last)
    last = now

print(times)
print("waiting for stuff to clear")
sleep(5)

times = []
print("running normal load")
for i in range(10):
    for j in range(50):
        with sentry_sdk.start_transaction(name='backpressure'):
            for i in range(10):
                with sentry_sdk.start_span(op='sleep', description='zzz'):
                    pass
    now = time()
    times.append(now - last)
    last = now
    sleep(5)

print(times)
sentry_sdk.flush(10)
