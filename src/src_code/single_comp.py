# file imports
import hashlib
import os
from src.src_code.file_object import dup_file
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

"""
Key Functionality:
---------------------------------------------------------------------------
- Logging File Setup

- Hashing Algorithm for files

- byte by byte comparison (todo)

- meta-data extraction (todo)

- meta-data comparison (todo)

- creation of dup_file instances

- function for parsing files in passed directory

- compares hashes of various files
---------------------------------------------------------------------------
"""

# number of works for pool_executor
num_workers = 5

# sets up logging file for application
def setup_logging():
    """
    Set up logging to a file named log.txt.

    Log messages will be written to this file.
    """
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)

    # Create a file handler that logs messages to log.txt
    file_handler = logging.FileHandler('log.txt')
    file_handler.setLevel(logging.INFO)  # Set the logging level for the file handler

    # Create a formatter and set it for the file handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

# computes file hash of file passed in
def compute_file_hash(filepath):

    """
    Computes the SHA-256 hash of a file.

    Args:
    filepath (str): The path to the file whose hash is to be computed.

    Returns:
    str: The hexadecimal string representation of the hash.
    """

    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    except IOError as e:
        logging.error(f"Error reading file {filepath}: {e}")
        return None

# todo
# byte by byte comparisons
def byte_by_byte():
    pass

## todo
# extracts metadata from file passed in 
def extract_metadata(filepath):

    pass

# todo
# compares meta data of two files
def compare_metadata(meta1, meta2):
    pass

# process new files and creates file_obj
def create_dup_file(entry):
    """
    Passes in entry from scandir operation

    Calculates hash of the document 

    Creates new dup_file instance and returns it
    """
    file_hash = compute_file_hash(entry.path)
    new_file = dup_file(entry.name, entry.path, file_hash)
    return new_file

# This function aggregates all files in directory into an array
def parse_files( directory_path ) :
    """
    Sets up the threads for execution

    Algorithm allows for recursive function that creates new dup_file objects for all files

    """
    file_list = {}

    with ThreadPoolExecutor(max_workers = num_workers) as executor:
        futures = []
        for entry in os.scandir(directory_path):

            if entry.is_file():
                future = executor.submit(create_dup_file, entry)
                futures.append(future)

            elif entry.is_dir():
                sub_file_map = parse_files(entry.path)
                file_list.update(sub_file_map)

        for future in as_completed(futures):
            file_obj = future.result()
            file_list[file_obj.get_hash()] = file_obj

    return file_list

# Runs comparison and groups duplicate files
def find_duplicate(directory_path):

    file_list = parse_files(directory_path)
    grouped_map = {}

    for key, value in file_list:
        f_hash = object.get_hash()
        


            