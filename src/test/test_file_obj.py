"""
This test file is used to test methods in file_obj.py file

Author: Garret Knapp
"""
import unittest
from src.src_code.file_object import dup_file

class TestFileObj(unittest.TestCase):

    def setUp(self):
        # Create a new instance of dup_file before each test
        self.test_file = dup_file("testfile.txt", "/path/to/file", "dfasddsaf")

    def test_name(self):
        self.assertEqual(self.test_file.get_name(), "testfile.txt")

    def test_get_path(self):
        self.assertEqual(self.test_file.get_path(), "/path/to/file")

    def test_get_file_hash(self):
        self.assertEqual(self.test_file.get_hash(), "dfasddsaf")

    def test_get_read(self):
        # Assuming get_read method exists to check the read status
        self.assertEqual(self.test_file.get_read(), False)

    def test_set_name(self):
        self.test_file.set_name("newname.txt")
        self.assertEqual(self.test_file.get_name(), "newname.txt")

    def test_set_path(self):
        self.test_file.set_path("/new/path/to/file.txt")
        self.assertEqual(self.test_file.get_path(), "/new/path/to/file.txt")

    def test_set_hash(self):
        self.test_file.set_hash("fedcba0987654321")
        self.assertEqual(self.test_file.get_hash(), "fedcba0987654321")

    def test_set_read(self):
        self.test_file.set_read()  # Assuming set_read accepts a parameter
        self.assertEqual(self.test_file.get_read(), True)

if __name__ == '__main__':
    unittest.main()