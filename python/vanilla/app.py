import pprint
import contextlib
import tracemalloc
import sentry_sdk

@contextlib.contextmanager
def measure():
    filters = [tracemalloc.Filter(True, '**sentry_sdk**')]

    if not tracemalloc.is_tracing():
        tracemalloc.start()

    snapshot1 = tracemalloc.take_snapshot().filter_traces(filters)

    yield

    snapshot2 = tracemalloc.take_snapshot().filter_traces(filters)
    snapshot = snapshot2.compare_to(snapshot1, 'lineno')
    pprint.pprint(snapshot)


sentry_sdk.init()

with measure():
    try:
        1 / 0
    except Exception:
        sentry_sdk.capture_exception()
