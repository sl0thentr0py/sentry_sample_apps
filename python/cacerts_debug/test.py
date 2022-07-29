import sentry_sdk

sentry_sdk.init(debug=True, ca_certs="/etc/ssl/certs/ca-certificates.crt")
sentry_sdk.capture_message("from python3:8:3 docker")
