FROM python:3.12.0-slim

RUN \
    set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
    python3-pip \
    build-essential \
    python3-venv \
    ffmpeg \
    git \
    nano \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip && pip3 install -U wheel && pip3 install -U setuptools==69.1.1
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt && rm -r /tmp/requirements.txt


COPY . /code
WORKDIR /code

CMD ["bash"]

