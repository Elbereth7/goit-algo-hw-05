from file_handler import load_logs
from collections import Counter

def filter_logs_by_level(logs: list, level: str) -> list:
# Using list comprehensions to create a list with all logs filtered by level.
    if logs:
        logs_by_level = [log for log in logs if log['level'] == level]
        return logs_by_level

def count_logs_by_level(logs: list) -> dict:
# Using list comprehensions to create a list of log levels and using collections Counter to get a dictionary with level counts
    if logs:
        level_list = [log['level'] for log in logs]
        level_count = dict(Counter(level_list))
        return level_count

def display_log_counts(counts: dict):
# Function accepts the dictionary with key value and counts of the key value and returns them in a readable format.
    first_column_header = 'Рівень логування'
    second_column_header = 'Кількість'
    first_column_length = len(first_column_header) + 1
    second_column_length = len(second_column_header) + 1
    print(f'{first_column_header} | {second_column_header}')
    print('-' * first_column_length + '|' + '-' * second_column_length)
    if counts:
        for level in counts:
            print(f'{level:<{first_column_length}}| {counts[level]:<{second_column_length-1}}')

def display_filtered_logs(logs: list, level: str):
    if logs:
        print(f"\nДеталі логів для рівня '{logs[0]['level']}':")
        for log in logs:
            print(' '.join(list(log.values())[:3]) + ' - ' + log['message'])
    else:
        print(f"\nРівень логів '{level}' не існує")

if __name__ == '__main__':
    print(filter_logs_by_level(load_logs('log_reader/logs.txt'), 'ERROR'))
    print(count_logs_by_level(load_logs('log_reader/logs.txt')))
    display_log_counts(count_logs_by_level(load_logs('log_reader/logs.txt')))
    display_filtered_logs(filter_logs_by_level(load_logs('log_reader/logs.txt'), 'ERROR'), 'ERROR')