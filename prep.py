# Function which will read config file and initialize file_path variables
import json
import glob
import os


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
    global deposit_latest_file
    deposit_latest_file = get_latest_log_file_deposit(deposit_task_log_path)
    print("The latest file from deposit to handle is " + deposit_latest_file)


def get_latest_log_file_deposit(deposit_task_log_path):

    deposit_most_recent_file = None
    deposit_most_recent_time = 0

    for entry in os.scandir(deposit_task_log_path):
        if entry.is_file():
            mod_time = entry.stat().st_mtime_ns
            if mod_time > deposit_most_recent_time:
                deposit_most_recent_file = entry.name
                deposit_most_recent_time = mod_time

    print("The latest file in the folder " + deposit_task_log_path + " is " + deposit_most_recent_file)
    return deposit_most_recent_file



def get_latest_log_file_loan(loan_task_log_path):

    loan_most_recent_file = None
    loan_most_recent_time = 0

    for entry in os.scandir(loan_task_log_path):
        if entry.is_file():
            mod_time = entry.stat().st_mtime_ns
            if mod_time > loan_most_recent_time:
                loan_most_recent_file = entry.name
                loan_most_recent_time = mod_time

    print("The latest file in the folder " + loan_task_log_path + " is " + loan_most_recent_file)
    return loan_most_recent_file
