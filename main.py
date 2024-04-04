# Entry point
import file_path_initializer


def welcome():
    print("Welcome to LogConverter app")
    print("Version: 1.0.0")
    file_path_initializer.init_path_variables()


welcome()
