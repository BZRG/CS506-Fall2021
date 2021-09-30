def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs((x[i] - y[i]))
    return res

def intersect(ls1, ls2):
    ls3 = [x for x in ls1 if x in ls2]
    return ls3

def jaccard_dist(x, y):
    x_modified = []
    y_modified = []
    for i in x:
        if i not in x_modified:
            x_modified.append(i)
    for i in y:
        if i not in y_modified:
            y_modified.append(i)
    
    inters = len(intersect(x_modified,y_modified))
    union = len(x_modified) + len(y_modified) - inters

    jaccard_idx = 0
    if union != 0:
        jaccard_idx = float(inters)/union

    return 1 - jaccard_idx


def cosine_sim(x, y):
    sum_xy = 0
    sum_x_sq = 0
    sum_y_sq = 0

    for i in range(len(x)):
        sum_xy += x[i]*y[i]
        sum_x_sq += x[i]**2
        sum_y_sq += y[i]**2
    
    sqrt_x = sum_x_sq**0.5
    sqrt_y = sum_y_sq**0.5
    denom = sqrt_x*sqrt_y
    cossim = 0
    if denom != 0:
        cossim = sum_xy/denom
    else:
        cossim = 'identical'
    return cossim

# Feel free to add more
