import random
import time
import logging

import pytest
import sentry_sdk
import pytest_sentry

logger = logging.getLogger(__name__)


@pytest.fixture()
def my_fixture():
    time.sleep(random.random())


def test_always_succeeds(my_fixture):
    time.sleep(random.random())
    assert True


def test_flaky():
    time.sleep(random.random())

    if random.random() < 0.80:
        assert False, "This is a flaky test"

    assert True


def test_always_fails():
    time.sleep(random.random())
    assert False


def test_logger_exception():
    # with pytest.raises(ValueError):
    #     raise ValueError("test")
    #
    sentry_sdk.capture_message("BOOGOO")

    assert True
