
import os
from dotenv import load_dotenv
import sys

class Reader:
    def __init__(self,  file_path=None):
        load_dotenv()
        self.file_path = file_path or os.path.join(os.path.dirname(__file__), "../test_cases", os.getenv("TEST_FILE", "data_tsp.txt"))
        self.buffer = []

    def buffer_read(self):
        with open(self.file_path, 'r') as file:
            self.buffer = file.readlines()
        return self.buffer
