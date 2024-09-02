import sentry_sdk
from opentelemetry import trace
from time import sleep

sentry_sdk.init(
    debug=True,
    traces_sample_rate=1.0,
)


with sentry_sdk.isolation_scope() as isolation_scope:
    print(sentry_sdk.get_isolation_scope()._tags)
    sentry_sdk.set_tag("a", 42)
    print(sentry_sdk.get_isolation_scope()._tags)
    print(isolation_scope._tags)
    with sentry_sdk.new_scope() as new_scope:
        new_scope.set_tag("b", 21)
        sentry_sdk.set_tag("c", "Asd")
        print(new_scope._tags)
        print(sentry_sdk.get_current_scope()._tags)
        print(sentry_sdk.get_isolation_scope()._tags)
        print(isolation_scope._tags)
