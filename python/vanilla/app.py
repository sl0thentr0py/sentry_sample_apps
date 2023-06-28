import linecache
import contextlib
import tracemalloc
import sentry_sdk
from threading import Thread, get_ident

sentry_sdk.init(traces_sample_rate=1.0, debug=True, send_default_pii=True)


def display_top(snapshot, limit=25):
    # just a helper for including the actual line of code instead of just
    # filename + line number and making the output more human friendly
    print("Top %s lines" % limit)
    for index, stat in enumerate(snapshot[:limit], 1):
        frame = stat.traceback[0]
        print(
            "#%s: %s:%s: %.1f KiB"
            % (
                index,
                frame.filename,
                frame.lineno,
                stat.size / 1024,
            )
        )
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print("    %s" % line)


@contextlib.contextmanager
def measure():
    filters = [tracemalloc.Filter(True, '**sentry_sdk**')]

    if not tracemalloc.is_tracing():
        tracemalloc.start()

    snapshot1 = tracemalloc.take_snapshot().filter_traces(filters)

    yield

    snapshot2 = tracemalloc.take_snapshot().filter_traces(filters)
    snapshot = snapshot2.compare_to(snapshot1, 'lineno')
    display_top(snapshot)


sentry_sdk.init()

def work():
    for i in range(10**3):
        print("%d: %d" % (get_ident(), i))
        with sentry_sdk.start_transaction(name='child transaction'):
            for i in range(1050):
                with sentry_sdk.start_span(op='sleep', description='zzz'):
                    2**10


with measure():
    for i in range(5):
        Thread(target=work).run()

sentry_sdk.flush(10)
