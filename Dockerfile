FROM alpine:3.20.0 as builder

RUN addgroup -S cfpredictorgroup && adduser -S cfpredictor -G cfpredictorgroup

WORKDIR /home/cfpredictor

RUN apk add --update --no-cache python3 clang pkgconfig && \
    python3 -m venv .venv && \
    /home/cfpredictor/.venv/bin/python3 -m ensurepip --upgrade && \
    /home/cfpredictor/.venv/bin/pip3 --no-cache install --upgrade pip setuptools && \
    /home/cfpredictor/.venv/bin/pip3 --no-cache install -r requirements.txt

FROM alpine:3.20.0

RUN addgroup -S cfpredictorgroup && adduser -S cfpredictor -G cfpredictorgroup && \
    apk add --update --no-cache python3

WORKDIR /home/cfpredictor

COPY --from=builder /home/cfpredictor/.venv/ /home/cfpredictor/.venv/
COPY run.py requirements.txt /home/cfpredictor/
COPY app ./app

USER cfpredictor

CMD [".venv/bin/python3", "run.py"]