from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers, validate_numbers
from pathlib import Path
import logging
import json

def main():
    cur_dir = Path.cwd()
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    filepath = Path(config["input_file"])
    logfilepath = Path(config["log_file"])
    logfilepath.parent.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=logfilepath,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding="utf-8"
    )
    logging.info("RUNNING...")

    if not filepath.exists():
        print(f"Файл {filepath} не существует.")
        logging.error(f"Файл {filepath} не существует.")

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
