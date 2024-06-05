FROM alpine:3.20.0 as builder

RUN addgroup -S cfpredictorgroup && adduser -S cfpredictor -G cfpredictorgroup

WORKDIR /home/cfpredictor

COPY requirements.txt /home/cfpredictor/

ENV PATH="/home/cfpredictor/.venv/bin:$PATH"

RUN apk add --update --no-cache python3 clang pkgconfig python3-dev && \
    python3 -m venv .venv && \
    python3 -m ensurepip --upgrade && \
    pip3 --no-cache install --upgrade pip setuptools && \
    pip3 --no-cache install -r requirements.txt

FROM alpine:3.20.0

ENV PATH="/home/cfpredictor/.venv/bin:$PATH"

RUN addgroup -S cfpredictorgroup && adduser -S cfpredictor -G cfpredictorgroup && \
    apk add --update --no-cache python3

WORKDIR /home/cfpredictor

COPY --from=builder /home/cfpredictor/.venv/ /home/cfpredictor/.venv/
COPY run.py requirements.txt /home/cfpredictor/
COPY app ./app

USER cfpredictor

CMD ["python3", "run.py"]