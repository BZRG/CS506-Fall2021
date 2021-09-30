def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    f = open(csv_file_path, 'r')
    lines = f.read().splitlines()
    mat = []
    for line in lines:
        matline = []
        for x in line.split(','):
            if x.isnumeric():
                matline.append(int(x))
            else:
                matline.append(x.replace('"',''))
        mat.append(matline)
    f.close()
    return mat
