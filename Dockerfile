FROM debian:bookworm-slim AS base

FROM base AS builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt
RUN apt-get update -y &&\
    apt-get -y --no-install-recommends install curl ca-certificates build-essential &&\ 
    curl -o bootstrap-salt.sh -L https://bootstrap.saltstack.com &&\
    bash bootstrap-salt.sh -U -M -X -d -D -P -x python3 stable 3007 &&\
    /opt/saltstack/salt/bin/python3 -m pip install --target=/install -r /requirements.txt

FROM base

EXPOSE 5678
COPY --from=builder /install /opt/saltstack/salt/lib/python3.10

ENV S6_OVERLAY_VERSION=3.2.0.0
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/opt/saltstack/salt/lib/python3.10

RUN apt-get -y update &&\
    apt-get -y --no-install-recommends install curl ca-certificates procps jq virt-what bats xz-utils &&\
    curl -o bootstrap-salt.sh -L https://bootstrap.saltstack.com &&\
    bash bootstrap-salt.sh -U -M -X -d -D -P -x python3 stable 3007 &&\
    curl -o /tmp/s6-overlay-noarch.tar.xz -L https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz &&\
    curl -o /tmp/s6-overlay-x86_64.tar.xz -L https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-x86_64.tar.xz &&\
    tar -Jxpf /tmp/s6-overlay-noarch.tar.xz -C / &&\
    tar -Jxpf /tmp/s6-overlay-x86_64.tar.xz -C / &&\
    # sed -i 's/CipherString = DEFAULT@SECLEVEL=2/CipherString = DEFAULT@SECLEVEL=1/' /etc/ssl/openssl.cnf &&\
    apt-get autoremove -y &&\
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "/init" ]
