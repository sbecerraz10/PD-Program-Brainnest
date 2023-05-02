list1 = [1, 2, 5]
list2 = [3, 4, 8]
res = [(a, b) for idx, a in enumerate(list1) for idx,b in enumerate(list2)]
print(res)