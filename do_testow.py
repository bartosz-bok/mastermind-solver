list1 = [[2, 1, 2, 1], [5, 1, 2, 1], [6, 1, 2, 1], [7, 1, 2, 1], [8, 1, 2, 1]]
list2 = [[2, 1, 2, 1], [5, 1, 2, 1], [6, 1, 2, 1], [7, 1, 2, 1], [8, 1, 2, 1]]


from itertools import combinations_with_replacement
import math

comb = combinations_with_replacement (['black','white',None], 4)
comb = list(comb)
comb = comb[2:]

# print(comb)

# Print the obtained combinations
for i in comb:
    print(list(i))

print(math.log2(1/1))