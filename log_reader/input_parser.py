from collections import defaultdict

def parse_log_line(line: str) -> dict:
# Parsing the log file line returning a dictionary with 'date', 'time', 'level' and 'message' keys
    logs = {}
    
    log_list = line.strip().split()
    log_list_length = len(log_list)
    logs['date'] = log_list[0]
    logs['time'] = log_list[1]
    logs['level'] = log_list[2]
    logs['message'] = " ".join(log_list[3:log_list_length])
    return logs

if __name__ == '__main__':
    line = '2024-01-22 08:30:01 INFO User logged in successfully.'
    print(parse_log_line(line))