FROM alpine:3.20.0

RUN addgroup -S cfpredictorgroup && adduser -S cfpredictor -G cfpredictorgroup

WORKDIR /home/cfpredictor

COPY run.py requirements.txt /home/cfpredictor/
COPY app ./app

RUN apk add --update --no-cache python3 clang && \
    python3 -m venv .venv && \
    /home/cfpredictor/.venv/bin/python3 -m ensurepip --upgrade && \
    /home/cfpredictor/.venv/bin/pip3 --no-cache install --upgrade pip setuptools && \
    /home/cfpredictor/.venv/bin/pip3 --no-cache install -r requirements.txt

USER cfpredictor

CMD ["python3", "run.py"]