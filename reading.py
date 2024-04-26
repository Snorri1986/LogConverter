# file contains functions for reading logs from txt

def read_deposit_log(latest_deposit_file_name):
    deposit_log_txt = open(latest_deposit_file_name, 'r')
    count = 0

    for line in deposit_log_txt:
        count += 1
        print("Line{}: {}".format(count, line.strip()))

    deposit_log_txt.close()

def read_loans_log(latest_loans_file_name):
        loans_log_txt = open(latest_loans_file_name, 'r')
        count = 0

        for line in loans_log_txt:
            count += 1
            print("Line{}: {}".format(count, line.strip()))

        loans_log_txt.close()