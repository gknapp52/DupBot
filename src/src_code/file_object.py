"""
This class is used to create an object to store attributes corresponding to a file. There are various getter and setters methods. 
The class has various attributes for the name of file, the path, the created hash, and if the file has been read yet.

Author: Garret Knapp
"""

class dup_file:
    def __init__(self, name, path, file_hash):
        self.name = name
        self._path = path
        self._file_hash = file_hash
        self._read = False

    # Getter Methods
    def get_name(self):
        return self.name

    def get_path(self):
        return self._path

    def get_hash(self):
        return self._file_hash

    def get_read(self):
        return self._read   
    
    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_path(self, path):
        self._path = path

    def set_hash(self, hash):
        self._file_hash = hash

    def set_read(self):
        if ( self._read == True):
            self._read = True
        else:
            self._read = True
