def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0], L[0])
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
        return (min, max)

# L = []
# print(findMinAndMax(L))

# L = [7]
# print(findMinAndMax(L))
# L = [7, 1]
# print(findMinAndMax(L))
L = [7, 1, 3, 9, 5]
print(findMinAndMax(L))