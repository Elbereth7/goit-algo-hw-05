from input_parser import parse_log_line

def load_logs(file_path: str) -> list:
# Завантаження лог-файлів виконує функція load_logs(file_path: str) -> list, 
# що відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line, 
# зберігаючи результати в список.


# Ваш скрипт повинен вміти обробляти різні види помилок, такі як відсутність файлу або помилки при його читанні. 
# Використовуйте блоки try/except для обробки виняткових ситуацій.
    try:
        with open(file_path, 'r') as file:
            parsed_logs = []
            lines = file.readlines()
            for line in lines:
                parsed_logs.append(parse_log_line(line))
        return parsed_logs
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    print(load_logs('log_reader/logs.txt'))