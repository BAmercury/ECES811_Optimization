from lin import polyhedron as ph
import numpy as np
from math import factorial
# A = [[-2, -1],
#     [-6, 1],
#     [1, -3],
#     [3, -2]]
# b = [-8, 2, -3, 9]
# c = '[<=,<=,<=,<=]'
# ans = ph.extreme_points(A,b,c)
# print(ans)

# B = [[1, -3], [3, -2], ]
# rank = np.linalg.matrix_rank(B)
# print(rank)

# A = [[1, 0, 0],
#     [1, 1, 0],
#     [0, 1, 1],
#     [1, 0, 1],
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1]]
# b = [1, 2, 2, 2, -1, -1, -1]
# c = '[<=,<=,<=,<=,>=,>=,>=]'
# ans = ph.extreme_points(A, b, c)
# #print(ans)
# new_array = [tuple(row) for row in ans]
# uniques = np.unique(new_array,axis=0)
# print(uniques)





A = np.array([
    [1,0,0,1,0,0,0,0,0,0],
    [1,1,0,0,1,0,0,0,0,0],
    [0,1,1,0,0,1,0,0,0,0],
    [1,0,1,0,0,0,1,0,0,0],
    [1,0,0,0,0,0,0,-1,0,0],
    [0,1,0,0,0,0,0,0,-1,0],
    [0,0,1,0,0,0,0,0,0,-1],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,1],

    ])
b = [1,2,2,2,-1,-1,-1,0,0,0,0,0,0,0]
c = '[=,=,=,=,=,=,=,>=,>=,>=,>=,>=,>=,>=]'
ans = ph.extreme_points(A,b,c)
new_array = [tuple(row) for row in ans]
uniques = np.unique(new_array, axis=0)
print(ans)


