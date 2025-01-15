import logging
import multiprocessing
import concurrent.futures
import sentry_sdk.integrations.logging

logging.captureWarnings(True)
logging.basicConfig(level=logging.DEBUG)

sentry_sdk.init(
    traces_sample_rate=1.0,
    integrations=[
        sentry_sdk.integrations.logging.LoggingIntegration(event_level=logging.WARNING),
    ]
)
sentry_sdk.capture_message("hello")

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    pool = concurrent.futures.ProcessPoolExecutor()
    pool.submit(sentry_sdk.capture_message, "world")
