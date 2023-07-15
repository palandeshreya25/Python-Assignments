# assignment 9
from operations import Operations, CustomException

obj = Operations()

try:
    obj.file_operations()
    obj.math_operations(25)
    obj.string_operations ('Hello world!')
    
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print("Caught CustomException:", e)
