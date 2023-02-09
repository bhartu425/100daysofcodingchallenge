from itertools import combinations
a = input()
ls = list(map(str, a.split()))
for i in range(1, int(ls[1])+1):
    ls2 = []
    ls2 = list(map("".join, combinations(ls[0], i)))
    for elem in ls2:
        ls2[ls2.index(elem)] = "".join(sorted(elem))
    ls2.sort()
    for char in ls2:
        print(char)
