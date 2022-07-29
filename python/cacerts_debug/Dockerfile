FROM python:3.8.3

WORKDIR /app

RUN pip install sentry-sdk

ARG SENTRY_DSN
ENV SENTRY_DSN=$SENTRY_DSN

COPY test.py test.py

CMD ["python", "test.py"]
