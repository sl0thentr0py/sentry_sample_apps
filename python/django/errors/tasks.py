from django_rq import job


@job
def foobar_task():
    a = 42
    raise Exception("Exception in rq_task")
    return 42
