"""CC-CEDIT Test."""

import unittest

from pycccedict.cccedict import CcCedict

class CcCedictTest(unittest.TestCase):
    """CC-CEDIT Test."""

    @classmethod
    def setUpClass(cls):
        cls.cccedict = CcCedict()

    def test_get_definitions(self):
        """Tests get_definitions"""
        self.assertEqual(self.cccedict.get_definitions('猫')[0], 'cat')

    def test_get_pinyin(self):
        """Tests get_pinyin"""
        self.assertEqual(self.cccedict.get_pinyin('猫'), 'mao1')

    def test_get_simplified(self):
        """Tests get_simplified"""
        self.assertEqual(self.cccedict.get_simplified('猫'), '猫')
        self.assertEqual(self.cccedict.get_simplified('貓'), '猫')

    def test_get_traditional(self):
        """Tests get_traditional"""
        self.assertEqual(self.cccedict.get_traditional('猫'), '貓')
        self.assertEqual(self.cccedict.get_traditional('貓'), '貓')

    def test_get_entry(self):
        """Tests get_entry."""
        for chinese in ['猫', '貓']:
            entry = self.cccedict.get_entry(chinese)
            for field in ['definitions', 'pinyin', 'simplified', 'traditional']:
                self.assertIn(field, entry)

    def test_get_entries(self):
        """Tests get_entries."""
        entries = self.cccedict.get_entries()
        for entry in entries:
            for field in ['definitions', 'pinyin', 'simplified', 'traditional']:
                self.assertIn(field, entry)

if __name__ == "__main__":
    unittest.main()
