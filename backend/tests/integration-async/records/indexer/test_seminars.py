#
# Copyright (C) 2021 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.
import orjson
from helpers.utils import retry_test
from inspirehep.records.api import SeminarsRecord
from inspirehep.search.api import SeminarsSearch
from invenio_db import db
from invenio_search import current_search
from tenacity import stop_after_delay, wait_fixed


def test_indexer_deletes_record_from_es(inspire_app, datadir):
    @retry_test(stop=stop_after_delay(30), wait=wait_fixed(2))
    def assert_record_is_deleted_from_es():
        current_search.flush_and_refresh("records-seminars")
        expected_records_count = 0
        record_lit_es = SeminarsSearch().get_record(str(record.id)).execute().hits
        assert expected_records_count == len(record_lit_es)

    data = orjson.loads((datadir / "1.json").read_text())
    record = SeminarsRecord.create(data)
    db.session.commit()

    record.delete()
    db.session.commit()

    assert_record_is_deleted_from_es()
