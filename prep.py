# Function which will read config file and initialize file_path variables
import json
import glob


deposit_task_log_path = None
loan_task_log_path = None
config_file_name = "config.json"

deposit_latest_file = None
loan_latest_file = None


def init_path_variables():
    config_json_f = open('config.json')
    config_in_dict = json.load(config_json_f)
    global deposit_task_log_path
    global loan_task_log_path
    deposit_task_log_path = config_in_dict['Locations']['deposit']
    loan_task_log_path = config_in_dict['Locations']['loans']
    config_json_f.close()
    print("For deposit_task_log_path set path to log file " + deposit_task_log_path)
    print("For loan_task_log_path set path to log file " + loan_task_log_path)
    get_latest_log_file_deposit(deposit_task_log_path)


def get_latest_log_file_deposit(deposit_task_log_path):
    deposit_log_files_list = glob.glob(deposit_task_log_path + "\\" + "V21Start-CvEod*.log")
    deposit_log_files_list_new = [w.replace("\\\\", "\\") for w in deposit_log_files_list]
    #TODO: get file only with latest creation date


def get_latest_log_file_loan(loan_task_log_path):
    var = None
    # TODO: finish the fuction
