FROM ubuntu:latest

RUN useradd -ms /bin/bash cfpredictor
WORKDIR /home/cfpredictor
COPY run.py .
COPY app ./app
COPY requirements.txt .

RUN apt update && apt install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

USER cfpredictor

WORKDIR /home/cfpredictor

CMD ["python3", "run.py"]
# ENTRYPOINT ["python3", "run.py"]