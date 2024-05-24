# file contains functions for reading logs from txt
import re
from datetime import datetime

pattern_to_find = r'\b(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b'

# Get the current timestamp in DD-MM-YYYY HH:MM:SS format
current_timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

def read_replace_deposit_log(latest_deposit_file_name,path_to_directory):
    deposit_log_lines = []
    # full path to file
    path_to_file = path_to_directory + '\\' + latest_deposit_file_name
    deposit_log_txt = open(path_to_file, 'r')
    count = 0

    # read
    for line in deposit_log_txt:
        deposit_log_lines = [line.strip() for line in deposit_log_txt]
        count += 1

    time_marks_list = []

    # find
    for string in deposit_log_lines:
        # Find all matches in the current string
        found = re.findall(pattern_to_find, string)
        # Add the matches to the list (flattening the result)
        time_marks_list.extend(found)

    # replace in a list
    modified_strings_list = []

    for string in time_marks_list:
        # Replace all matches with the current timestamp
        modified_string = re.sub(pattern_to_find, current_timestamp, string)
        # Add the modified string to the list
        modified_strings_list.append(modified_string)

    # replace in a file
    #deposit_log_txt.close()



    #deposit_log_txt.close() # close as a read
    #print(deposit_log_lines)
    #print(matches)
    #print(modified_strings_list)

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


