import logging
import time
import sentry_sdk
from secrets import token_hex
from celery import Celery, signals


def init_sentry():
    sentry_sdk.init(debug=True)


# init_sentry()


app = Celery(
    'celery',
    broker='redis://localhost:6379',
    include=['tasks'],
)

logger = logging.getLogger(__name__)
logger.error(f"SETUP {token_hex(2)}")


@app.task
def my_task():
    logger.error(f"MY_TASK {token_hex(2)}")


@signals.celeryd_init.connect
# @signals.worker_init.connect
def init_worker(**_kwargs):
    init_sentry()
