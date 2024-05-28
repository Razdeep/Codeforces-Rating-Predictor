FROM alpine:3.20.0

RUN addgroup -S cfpredictorgroup && adduser -S cfpredictor -G cfpredictorgroup

WORKDIR /home/cfpredictor

COPY run.py .
COPY app ./app
COPY requirements.txt .

RUN apk add --update --no-cache python3 && \
    python3 -m pip --no-cache install -r requirements.txt

USER cfpredictor

WORKDIR /home/cfpredictor

CMD ["python3", "run.py"]