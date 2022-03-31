import unittest
from unittest.mock import patch
import src.app

class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    def test_get_doc_owner_name(self):
        with patch('builtins.input', side_effect=['10006']):
            self.assertEqual(src.app.get_doc_owner_name(), 'Аристарх Павлов')

    def test_delete_doc(self):
        with patch('builtins.input', side_effect=['11-2']):
            self.assertEqual(src.app.delete_doc(), ('11-2', True))

    def test_add_new_doc(self):
        with patch('builtins.input', side_effect=['123', 'passport', 'Boris', '24']):
            self.assertEqual(src.app.add_new_doc(), '24')

if __name__ == '__main__':
    unittest.main()



