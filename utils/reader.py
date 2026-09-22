def read_numbers(file_path):
    a= []
    with open(file_path) as f:
        for s in f:
            s = s.strip()
            if s:
                a.append(float(s))
    return a