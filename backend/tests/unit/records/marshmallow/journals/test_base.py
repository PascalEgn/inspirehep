#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.
from inspirehep.records.marshmallow.journals.base import (
    JournalsAdminSchema,
    JournalsPublicSchema,
)


def test_admin_schema():
    expected_result = {
        "_private_notes": "PRIVATE",
        "_collections": ["collection1, collection2"],
        "journal_title": {"title": "Journal of Physical Science and Application"},
        "short_title": "J.Phys.Sci.Appl.",
    }

    data = {
        "_private_notes": "PRIVATE",
        "_collections": ["collection1, collection2"],
        "journal_title": {"title": "Journal of Physical Science and Application"},
        "short_title": "J.Phys.Sci.Appl.",
    }

    result = JournalsAdminSchema().dump(data).data
    assert expected_result == result


def test_public_schema():
    expected_result = {
        "number_of_papers": 2137,
        "journal_title": {"title": "Journal of Physical Science and Application"},
        "short_title": "J.Phys.Sci.Appl.",
    }

    data = {
        "number_of_papers": 2137,
        "_private_notes": "PRIVATE",
        "_collections": ["collection1, collection2"],
        "journal_title": {"title": "Journal of Physical Science and Application"},
        "short_title": "J.Phys.Sci.Appl.",
    }

    result = JournalsPublicSchema().dump(data).data
    assert expected_result == result
