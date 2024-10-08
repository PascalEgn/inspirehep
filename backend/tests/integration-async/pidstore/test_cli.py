#
# Copyright (C) 2021 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.
from helpers.utils import create_record
from invenio_pidstore.models import PersistentIdentifier


def test_fast_bai_minter_cli(inspire_app, cli, override_config):
    with override_config(
        FEATURE_FLAG_ENABLE_BAI_PROVIDER=True,
        FEATURE_FLAG_ENABLE_BAI_CREATION=False,
        FEATURE_FLAG_ENABLE_AUTHOR_DISAMBIGUATION=False,
    ):
        create_record("aut")
        create_record(
            "aut", data={"ids": [{"value": "M.Moskovic.1", "schema": "INSPIRE BAI"}]}
        )

        assert (
            PersistentIdentifier.query.filter_by(pid_type="aut", status="R").count()
            == 2
        )
        assert (
            PersistentIdentifier.query.filter_by(pid_type="bai", status="R").count()
            == 1
        )

        with override_config(
            FEATURE_FLAG_ENABLE_BAI_CREATION=True, FEATURE_FLAG_ENABLE_BAI_PROVIDER=True
        ):
            cli.invoke(["inspire-pidstore", "fast-mint-new-bais", "--yes-i-know"])

        assert (
            PersistentIdentifier.query.filter_by(pid_type="aut", status="R").count()
            == 2
        )
        assert (
            PersistentIdentifier.query.filter_by(pid_type="bai", status="R").count()
            == 2
        )
