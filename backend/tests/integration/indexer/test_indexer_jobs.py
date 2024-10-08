#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from copy import deepcopy

from helpers.utils import create_record, es_search
from marshmallow import utils


def test_index_job_record(inspire_app):
    record = create_record(
        "job", data={"acquisition_source": {"orcid": "0000-0000-0000-0000"}}
    )

    expected_total = 1
    expected_source = deepcopy(record)
    expected_source["_created"] = utils.isoformat(record.created)
    expected_source["_updated"] = utils.isoformat(record.updated)

    response = es_search("records-jobs")
    response_source = response["hits"]["hits"][0]["_source"]
    response_total = response["hits"]["total"]["value"]

    assert expected_total == response_total
    assert expected_source == response_source
