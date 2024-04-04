# Function which will read config file and initialize file_path variables
import json

deposit_task_log_path = None
loan_task_log_path = None
config_file_name = "config.json"


def init_path_variables():
    config_json_f = open('config.json')
    config_in_dict = json.load(config_json_f)
    global deposit_task_log_path
    global loan_task_log_path
    deposit_task_log_path = config_in_dict['Locations']['deposit']
    loan_task_log_path = config_in_dict['Locations']['loans']
    print("For deposit_task_log_path set path to log file " + deposit_task_log_path)
    print("For loan_task_log_path set path to log file " + loan_task_log_path)
