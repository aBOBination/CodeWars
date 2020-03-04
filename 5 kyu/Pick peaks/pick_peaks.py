from functools import reduce
def map_test(x, y):

    if x < y:
        peaks = []
        peaks.append(y)
    else:
        valley = []
        peaks.append(x)
    return peaks


y = [1, 2, 3, 4, 4, 4, 5, 4, 3, 2, 3, 4, 5, 4]


z = reduce(map_test, y)


print(z)
