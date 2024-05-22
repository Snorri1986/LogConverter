# file contains functions for reading logs from txt

def read_deposit_log(latest_deposit_file_name,path_to_directory):
    deposit_log_lines = []
    # full path to file
    path_to_file = path_to_directory + '\\' + latest_deposit_file_name
    deposit_log_txt = open(path_to_file, 'r')
    count = 0

    for line in deposit_log_txt:
        deposit_log_lines = [line.strip() for line in deposit_log_txt]
        count += 1

    deposit_log_txt.close()


def read_loans_log(latest_loans_file_name,path_to_directory):
    loans_log_lines = []
    # full path to file
    path_to_file = path_to_directory + '\\' + latest_loans_file_name
    loans_log_txt = open(path_to_file, 'r')
    count = 0

    for line in loans_log_txt:
        loans_log_lines = [line.strip() for line in loans_log_txt]
        count += 1

    loans_log_txt.close()
