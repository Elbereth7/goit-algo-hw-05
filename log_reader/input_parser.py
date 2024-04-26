def parse_log_line(line: str) -> dict:
# Парсинг рядка логу виконує функцію parse_log_line(line: str) -> dict, 
# яка приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: 
# дата, час, рівень, повідомлення. Використовуйте методи рядків, такі як split(), для розділення рядка на частини.
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