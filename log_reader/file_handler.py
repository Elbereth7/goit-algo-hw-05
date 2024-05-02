from input_parser import parse_log_line

def load_logs(file_path: str) -> list:
# Using list comprehensions to create a list of parsed logs from a file
# In case of missing file or reading error the error log will be displayed
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            parsed_logs = [parse_log_line(line) for line in lines]
        return parsed_logs
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    print(load_logs('log_reader/logs.txt'))