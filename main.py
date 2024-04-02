# Entry point
def welcome():
    print("Welcome to LogConverter app")


def get_log_path():
    print("Please enter log location using \\ like separator ")
    file_path = input("Enter file path here: ")
    print("You enetered " + file_path)
    return file_path


welcome()
log_path = get_log_path()
