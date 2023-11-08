FROM python:3.8.16-slim-buster

RUN pip install sentry-sdk

COPY app.py .

ARG SENTRY_DSN
ENV SENTRY_DSN=$SENTRY_DSN

CMD ["python", "app.py"]
# CMD ["/bin/bash"]
