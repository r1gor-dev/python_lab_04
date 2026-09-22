from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers
# from utils.statistics import find_min
# from utils.statistics import find_max
def main():
    a =read_numbers("data/measurements.txt")
    print(calculate_average(a))
    print(find_min(a))
    print(find_max(a))

# PEP 8 tabs
if __name__ == "__main__":
    main()