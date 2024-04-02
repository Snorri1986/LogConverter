import unittest

# Entry point
def welcome():
    print("Welcome to LogConverter app")


#TODO: add check by NULL
def get_log_path():
    print("Please enter log location using \\ like separator ")
    file_path = input("Enter file path here: ")
    print("You enetered " + file_path)
    return file_path


welcome()
log_path = get_log_path()

#TODO: finish unit test
class Testing(unittest.TestCase):
    def test_get_log_path(self):
        test_log_path=get_log_path()

