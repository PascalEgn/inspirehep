#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from flask import current_app
from inspirehep.search.factories.query import inspire_query_factory
from mock import patch
from opensearch_dsl import Search


@patch("inspirehep.search.factories.query.inspire_query_parser.parse_query")
def test_inspire_query_parser_is_called(mock_inspire_query_parser, inspire_app):
    query_string = "foo"
    with current_app.test_request_context():
        factory = inspire_query_factory()
        search = Search()

        factory(query_string, search)

        mock_inspire_query_parser.assert_called_once_with(query_string)


def test_inspire_query_parser_max_recursion_on_complicated_queries(inspire_app):
    query_string = "find a name" + " or a name" * 250
    with current_app.test_request_context():
        factory = inspire_query_factory()
        search = Search()

        factory(query_string, search)
