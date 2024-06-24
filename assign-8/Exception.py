# Custom exception class
import os
import pandas as pd 
class DataCleaningError(Exception):
    def __init__(self, message="Error during data cleaning"):
        self.message = message
        super().__init__(self.message)