"""Contains file-handling classes for Python 3."""

import os
import os.path

def ensure_dir(dir_name):
    """Checks if C{dir_name} directory exists, and if not, creates it.
    @return C{True} on success; C{False} otherwise."""
    if not os.path.isdir(dir_name):
        if os.path.exists(dir_name):
            return False
        else:
            os.mkdir(dir_name)
    return True

class FileStreamHandler(object):
    def __init__(self, file_name, encoding = 'utf-8'):
        """Guess."""
        self.file_name = file_name
        self.encoding = encoding
        self.stream = None
    
    def __del__(self):
        self.close()
    
    def open(self):
        """Opens the file. Implemented in the subclasses."""
        raise NotImplementedError
    
    def close(self):
        """Closes the file."""
        if self.stream:
            self.stream.close()
            self.stream = None
    
class FileReader(FileStreamHandler):
    def __init__(self, file_name, encoding = 'utf-8'):
        """Guess."""
        FileStreamHandler.__init__(self, file_name, encoding)
        
    def open(self):
        """Opens the file for reading."""
        self.stream = open(self.file_name, 'r', encoding = self.encoding)
        return self
    
    def __iter__(self):
        """Iterates through the lines in the file."""
        return self.stream.__iter__()
    
class FileWriter(FileStreamHandler):
    def __init__(self, file_name, encoding = 'utf-8'):
        """Guess."""
        FileStreamHandler.__init__(self, file_name, encoding)
        
    def open(self):
        """Opens the file for writing."""
        self.stream = open(self.file_name, 'w', encoding = self.encoding)
        return self
    
    def write(self, text):
        """Writes C{text} to the file in the correct encoding."""
        self.stream.write(text)
