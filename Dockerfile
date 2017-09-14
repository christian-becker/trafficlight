# start with Alpine Linux for ARMv6 32-bit (Raspberry Pi Zero or better)
FROM arm32v6/alpine
MAINTAINER Christian Becker <mail@christianbecker.name>

# system setup with "trafficlight" and requirements (Python modules for Pimoroni Blinkt!)
RUN apk add --no-cache \
        gcc \
        git \
        musl-dev \
        python3 \
        python3-dev \
    && pip3 install --no-cache-dir blinkt \
    && git clone https://github.com/christian-becker/trafficlight.git \
    && rm -R /trafficlight/.git* \
    && apk del gcc git musl-dev python3-dev \
    && echo "! installation is finished !"

# run trafficlight
CMD ["/trafficlight/trafficlight.py"]
