import sys
from pathlib import Path
import data_handler as dh
from file_handler import load_logs

def main():
# Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
# python [main.py](<http://main.py/>) /path/to/logfile.log
# Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        if load_logs(path):
            dh.display_log_counts(dh.count_logs_by_level(load_logs(path)))
        # Скрипт повинен приймати не обов'язковий аргумент командного рядка, 
        # після аргументу шляху до файлу логів. Він відповідає за виведення всіх записи певного рівня логування. 
        # І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
        # python main.py path/to/logfile.log error
            if len(sys.argv) > 2:
                level = sys.argv[2].upper()
                dh.display_filtered_logs(dh.filter_logs_by_level(load_logs(path), level), level)
    else:
        print('No argument entered. Please enter a log file path as an argument')


# При розробці обов'язково було використано один з елементів функціонального програмування: лямбда-функція, списковий вираз, функція filter, тощо.

if __name__ == '__main__':
    main()





