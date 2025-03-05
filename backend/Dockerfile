# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

FROM registry.cern.ch/cern-sis/base-images/python:3.11

WORKDIR /opt/inspire

ENTRYPOINT ["uv", "run", "inspirehep"]
CMD ["shell"]

ENV PYTHONBUFFERED=0 \
    SSL_CERT_FILE="/etc/ssl/certs/ca-certificates.crt" \
    REQUESTS_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt" \
    PATH="/root/.local/bin:${PATH}"

COPY CERN_Root_Certification_Authority_2.pem /usr/local/share/ca-certificates/CERN_Root_Certification_Authority_2.crt

RUN apt-get update && \
    apt-get install -y libpq-dev poppler-utils && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates && \
    pip config set global.cert "${REQUESTS_CA_BUNDLE}"

RUN curl -LsSf https://astral.sh/uv/0.6.3/install.sh | sh && uv --version
COPY uv.lock pyproject.toml ./

COPY gunicorn_config.py ./
COPY inspirehep inspirehep/
COPY tests tests/
COPY scripts scripts/
COPY data data/

ARG VERSION
ENV VERSION="${VERSION}"

RUN uv sync --system
