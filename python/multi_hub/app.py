import sentry_sdk

DSN1 = "https://2fb45f003d054a7ea47feb45898f7649@o447951.ingest.sentry.io/5434472"
DSN2 = "https://d655584d05f14c58b86e9034aab6817f@o447951.ingest.sentry.io/5461230"

first_client = sentry_sdk.init(DSN1, debug=True)
second_client = sentry_sdk.Hub(sentry_sdk.Client(DSN2, debug=True))

# try:
#     1 / 0
# except Exception as e:
#     sentry_sdk.capture_exception(e)


with second_client:
    l = {}
    try:
        x = l['adasdasdasdas']
    except Exception as e:
        sentry_sdk.capture_exception(e)

second_client.flush()
