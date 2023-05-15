from django_rq import job
from celery import shared_task


@job
def rq_task():
    a = 42
    raise Exception("Exception in rq_task")
    return 42


@shared_task
def celery_task():
    a = 42
    raise Exception("Exception in celery_task")
    return 42


@shared_task
def tell_the_world(msg):
    print("Thats my message to the world: %s" % msg)

