# -*- coding: utf-8 -*-

import unittest
from .estestcase import ESTestCase
from pyes.query import TermQuery

class MultifieldTestCase(ESTestCase):
    def setUp(self):
        super(MultifieldTestCase, self).setUp()
        mapping = {'parsedtext': {'boost': 1.0,
                                   'index': 'analyzed',
                                   'store': 'yes',
                                   'type': 'string',
                                   "term_vector": "with_positions_offsets"},
                   'title': {'boost': 1.0,
                              'index': 'analyzed',
                              'store': 'yes',
                              'type': 'string',
                              "term_vector": "with_positions_offsets"},
                   'name': {"type": "multi_field",
                             "fields": {
                                 'name': {
                                     'boost': 1.0,
                                     'index': 'analyzed',
                                     'omit_norms': False,
                                     'omit_term_freq_and_positions': False,
                                     'store': 'yes',
                                     "term_vector": "with_positions_offsets",
                                     'type': 'string'},
                                 'untouched': {'boost': 1.0,
                                                'index': 'not_analyzed',
                                                'omit_norms': False,
                                                'omit_term_freq_and_positions': False,
                                                'store': 'yes',
                                                "term_vector": "no",
                                                'type': 'string'}

                             }

                   },

                   'pos': {'store': 'yes',
                            'type': 'integer'},
                   'uuid': {'boost': 1.0,
                             'index': 'not_analyzed',
                             'store': 'yes',
                             'type': 'string'}}
        self.conn.create_index(self.index_name)
        self.conn.put_mapping(self.document_type, {'properties': mapping}, self.index_name)
        self.conn.index({"name": "Joe Tester", "parsedtext": "Joe Testere nice guy", "uuid": "11111", "position": 1},
            self.index_name, self.document_type, 1)
        self.conn.index({"name": "Bill Baloney", "parsedtext": "Joe Testere nice guy", "uuid": "22222", "position": 2},
            self.index_name, self.document_type, 2)
        self.conn.index({"value": "Joe Tester"}, self.index_name, self.document_type)
        self.conn.index({"value": 123343543536}, self.index_name, self.document_type)
        self.conn.index({"value": True}, self.index_name, self.document_type)
        self.conn.index({"value": 43.32}, self.index_name, self.document_type)
        #self.conn.index({"value": datetime.now()}, self.index_name, self.document_type)
        self.conn.refresh(self.index_name)

    def test_TermQuery(self):
        q = TermQuery("name", "joe")
        resultset = self.conn.search(query=q, indices=self.index_name)
        self.assertEquals(resultset.total, 1)

        q = TermQuery("name", "joe", 3)
        resultset = self.conn.search(query=q, indices=self.index_name)
        self.assertEquals(resultset.total, 1)

        q = TermQuery("name", "joe", "3")
        resultset = self.conn.search(query=q, indices=self.index_name)
        self.assertEquals(resultset.total, 1)

        q = TermQuery("value", 43.32)
        resultset = self.conn.search(query=q, indices=self.index_name)
        self.assertEquals(resultset.total, 1)


if __name__ == "__main__":
    unittest.main()
