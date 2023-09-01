from celery import Celery, signals
import sentry_sdk


app = Celery(
    'celery',
    broker='redis://localhost:6379',
    include=['tasks'],
)


def init_sentry():
    sentry_sdk.init(traces_sample_rate=1.0, debug=True)


@signals.celeryd_init.connect
def init_worker(**_kwargs):
    init_sentry()
