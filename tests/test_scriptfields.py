# -*- coding: utf-8 -*-

import unittest
from pyes import scriptfields

class ScriptFieldsTest(unittest.TestCase):
    def test_scriptfieldserror_imported(self):
        self.assertTrue(hasattr(scriptfields, 'ScriptFieldsError'))


if __name__ == '__main__':
    unittest.main()
