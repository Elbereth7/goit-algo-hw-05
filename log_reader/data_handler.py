from file_handler import load_logs

def filter_logs_by_level(logs: list, level: str) -> list:
# Фільтрацію за рівнем логування виконує функція filter_logs_by_level(logs: list, level: str) -> list. 
# Вона дозволить вам отримати всі записи логу для певного рівня логування.
    logs_by_level = []
    for log in logs:
        if log['level'] == level:
            logs_by_level.append(log)
    return logs_by_level

def count_logs_by_level(logs: list) -> dict:
# Підрахунок записів за рівнем логування повинна робити функція count_logs_by_level(logs: list) -> dict, 
# яка проходить по всім записам і підраховує кількість записів для кожного рівня логування.
    # First way - using dictionary for checking if value is unique and incrementing level counts
    # level_count = {}
    # for log in logs:        
    #     if log['level'] in level_count:
    #         level_count[log['level']] += 1
    #     else:
    #         level_count[log['level']] = 1
    # return level_count

    # Second way - using set for getting unique levels and reusing filter_logs_by_level() 
    # function to check the length of a filtered logs
    level_count = {}
    level_set = set()
    for log in logs: 
        level_set.add(log['level'])
        for level in level_set:
            qty = len(filter_logs_by_level(logs, level))
            level_count[level] = qty
    return level_count

def display_log_counts(counts: dict):
# Вивід результатів виконайте за допомоги функції display_log_counts(counts: dict), 
# яка форматує та виводить результати підрахунку в читабельній формі.
# Вона приймає результати виконання функції count_logs_by_level.
    first_column_header = 'Рівень логування'
    second_column_header = 'Кількість'
    first_column_length = len(first_column_header) + 1
    second_column_length = len(second_column_header) + 1
    print(f'{first_column_header} | {second_column_header}')
    print('-' * first_column_length + '|' + '-' * second_column_length)
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
    display_filtered_logs(filter_logs_by_level(load_logs('log_reader/logs.txt'), 'ERROR'))