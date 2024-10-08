#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


import requests
import structlog
from flask import current_app
from invenio_pidstore.models import PIDStatus, RecordIdentifier

from inspirehep.pidstore.providers.base import InspireBaseProvider

LOGGER = structlog.getLogger()


def get_next_pid_from_legacy():
    """Reserve the next pid on legacy.
    Sends a request to a legacy instance to reserve the next available
    identifier, and returns it to the caller.
    """
    headers = {
        "User-Agent": "invenio_webupload",
        "Authorization": (
            f"Bearer {current_app.config.get('BATCHUPLOADER_WEB_ROBOT_TOKEN', '')}"
        ),
    }

    url = current_app.config.get("LEGACY_PID_PROVIDER")
    next_pid = requests.get(url, headers=headers).json()
    return next_pid


class InspireRecordIdProvider(InspireBaseProvider):
    """Record identifier provider."""

    pid_type = None

    pid_provider = "recid"

    default_status = PIDStatus.RESERVED

    @classmethod
    def create(cls, object_type=None, object_uuid=None, **kwargs):
        """Create a new record identifier."""
        pid_value = kwargs.get("pid_value")
        if pid_value is None:
            if current_app.config.get("LEGACY_PID_PROVIDER"):
                kwargs["pid_value"] = get_next_pid_from_legacy()
                LOGGER.info("Control number from legacy", recid=kwargs["pid_value"])
                RecordIdentifier.insert(kwargs["pid_value"])
            else:
                kwargs["pid_value"] = str(RecordIdentifier.next())
                LOGGER.info(
                    "Control number from RecordIdentifier", recid=kwargs["pid_value"]
                )
        else:
            LOGGER.info("Control number provided", recid=kwargs["pid_value"])
            RecordIdentifier.insert(kwargs["pid_value"])

        kwargs.setdefault("status", cls.default_status)
        if object_type and object_uuid:
            kwargs["status"] = PIDStatus.REGISTERED
        return super().create(
            object_type=object_type, object_uuid=object_uuid, **kwargs
        )
