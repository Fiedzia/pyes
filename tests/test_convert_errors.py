# -*- coding: utf-8 -*-

import unittest
from .estestcase import ESTestCase
from pyes.exceptions import (NotFoundException, IndexAlreadyExistsException)
from pyes import convert_errors


class RaiseIfErrorTestCase(ESTestCase):
    def test_not_found_exception(self):
        self.assertRaises(
            NotFoundException,
            convert_errors.raise_if_error,
            404, {'_type': 'a_type', '_id': '1', '_index': '_all'})

    def test_nested_index_already_exists_exception(self):
        self.assertRaises(
            IndexAlreadyExistsException,
            convert_errors.raise_if_error,
            400, {'status': 400,
                  'error': ('RemoteTransportException[[name][inet' +
                             '[/127.0.0.1:9300]][indices/createIndex]]; ' +
                             'nested: IndexAlreadyExistsException[' +
                             '[test-index] Already exists]; ')})

if __name__ == '__main__':
    unittest.main()
