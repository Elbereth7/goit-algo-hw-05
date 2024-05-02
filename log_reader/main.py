import sys
from pathlib import Path
import data_handler as dh
from file_handler import load_logs

def main():
# Accepts the second terminal argument as a file path to logs file and returns the counter of each log level (INFO, ERROR, DEBUG, WARNING) from a file
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        if load_logs(path):
            dh.display_log_counts(dh.count_logs_by_level(load_logs(path)))
            # If log level is provided as a third argument in a terminal all the relevant level logs are displayed
            if len(sys.argv) > 2:
                level = sys.argv[2].upper()
                dh.display_filtered_logs(dh.filter_logs_by_level(load_logs(path), level), level)
    else:
        print('No argument entered. Please enter a log file path as an argument')


if __name__ == '__main__':
    main()





