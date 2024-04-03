# Function which will read config file and initialize file_path variables
import json

deposit_task_log_path = None
loan_task_log_path = None
config_file_name = "config.json"


# TODO: read data from config.file
def init_path_variables():
    config_json_f = open('config.json')
    config_in_dict = json.load(config_json_f)
    print(config_in_dict)  # temporary test code
