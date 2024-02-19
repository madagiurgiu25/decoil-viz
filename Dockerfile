FROM decoil-base:1.0.2_411

ENV DEBIAN_FRONTEND=noninteractive

ARG VERSION_DECOILVIZ
LABEL "decoil-viz"=${VERSION_DECOILVIZ}
LABEL "desc"="Decoil-viz environment"

RUN apt-get -y update \
    && apt-get install -y --no-install-recommends libssl-dev software-properties-common build-essential libstdc++6 pandoc openssh-server gcc g++ \
    && apt-get install -y zlib1g-dev libcurl4-openssl-dev python3-pip python3-dev \
    && apt-get clean -y \
    && rm -rf /var/cache/apt/archives /var/lib/apt/lists/*


RUN mkdir -p /code
COPY . /code

RUN cd /code && \
    python3 -m pip uninstall decoil-viz -y && \
    python3 -m pip install --no-cache-dir setuptools && \
    python3 -m pip install --no-cache-dir . && \
    python3 setup.py build install

CMD ["decoil-viz"]