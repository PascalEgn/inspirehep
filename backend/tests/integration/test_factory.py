#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


def test_http_response_with_different_host_name_and_server_name(inspire_app):
    headers = {"Host": "foo.bar"}

    expected_status_code = 200
    with inspire_app.test_client() as client:
        response = client.get("/ping", headers=headers)
    response_status_code = response.status_code

    assert expected_status_code == response_status_code
