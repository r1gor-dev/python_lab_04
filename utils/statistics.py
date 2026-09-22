def calculate_average(measurements):
    return sum(measurements)/len(measurements) if measurements else 0

def find_min(measurements):
    return min(measurements) if measurements else 0

def find_max(measurements):
    return max(measurements) if measurements else 0

# можно было и старые функции из лабораторной работы номер 3, но они медленнее