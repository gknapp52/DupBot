"""
This file tests the functions within the single_comp.py

Author: Garret Knapp
"""

import unittest
from src.src_code.single_comp import setup_logging
from src.src_code.single_comp import compute_file_hash
from src.src_code.single_comp import create_dup_file
from src.src_code.single_comp import parse_files
from src.src_code.single_comp import hash_cmp_func
import logging
import os

class TestSetupLogging(unittest.TestCase):

    def test_setup_logging(self):

        setup_logging()

        self.assertTrue(os.path.isfile('log.txt'))

    def tearDown(self):
        # This method will run after each test method
        logging.shutdown()

        if os.path.exists('log.txt'):
            os.remove('log.txt')

class TestHashingMethod(unittest.TestCase):
    
    def test_the_hash(self):

        test_output = compute_file_hash("C:\\Users\\garre\\Periscope\\DupBot\\src\\src_code\\file_object.py")
        self.assertIsNotNone(test_output)
        test_output_dos = compute_file_hash("C:\\Users\\garre\\Periscope\\DupBot\\src\\src_code\\file_object.py")
        self.assertEqual(test_output, test_output_dos)

class TestParseFile_dupfile(unittest.TestCase):
    
    def test_dup_file_creation():
        pass

    def parse_file():
        pass

if __name__ == '__main__':
    unittest.main()