#assignment 9
import math

class Operations:
    def __init__(self):
        self.file_modes = 'Shreya'
    
    def file_operations(self):
        print("File Modes:", self.file_modes)
    
    def math_operations(self, number):
        print("Square root of", number, "is", math.sqrt(number))
    
    def string_operations(self, text):
        words = text.split()
        print("Words in the text:", words)


class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message