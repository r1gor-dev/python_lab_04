from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers, validate_numbers
from pathlib import Path
import logging
import json

def main():
    cur_dir = Path.cwd()
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding="utf-8"
    )
    logging.info("RUNNING...")

    print(cur_dir)

    # filepath = Path("data/measurements.txt")
    filepath = config["input_file"]
    logfilepath = config["log_file"]
    #print(filepath.exists())


    logsdir = Path("logs")
    logsdir.mkdir(exist_ok=True)
    try:
        a =read_numbers(filepath)
        validate_numbers(a)
        print("Успешно прочитан файл")
        logging.info(f"Успешно прочитан файл, прочитано {len(a)} значений.")
        print(calculate_average(a))
        print(find_min(a))
        print(find_max(a))
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        logging.error(f"Файл {filepath} не найден.")
    except ValueError:
        print(f"Файл {filepath} невозможно прочитать.")
        logging.error(f"Файл {filepath} невозможно прочитать.")
    finally:
        logging.info("...SHUTTING DOWN...")

# PEP 8 tabs
if __name__ == "__main__":
    main()
