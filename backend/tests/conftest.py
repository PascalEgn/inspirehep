#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import pytest


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "filter_query_parameters": ["access_token"],
        "ignore_localhost": True,
        "decode_compressed_response": True,
        "filter_headers": ("Authorization", "User-Agent"),
        "ignore_hosts": (
            "cache",
            "db",
            "es",
            "flower",
            "indexer",
            "localhost",
            "mq",
            "postgres",
            "redis",
            "ui",
            "next-web",
            "web-worker",
            "web",
            "worker",
        ),
        "record_mode": "once",
    }


@pytest.fixture(scope="module")
def es(appctx):
    """Setup all registered Elasticsearch indices."""
    from invenio_search import current_search_client

    return current_search_client
