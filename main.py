from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers
from pathlib import Path

def main():
    cur_dir = Path.cwd()
    print(cur_dir)

    filepath = Path("data/measurements.txt")
    print(filepath.exists())

    logsdir = Path("logs")
    logsdir.mkdir(exist_ok=True)
    try:
        a =read_numbers(filepath)
        print("all ok.")
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except ValueError:
        print(f"Файл {filepath} невозможно прочитать.")

    print(calculate_average(a))
    print(find_min(a))
    print(find_max(a))

# PEP 8 tabs
if __name__ == "__main__":
    main()
