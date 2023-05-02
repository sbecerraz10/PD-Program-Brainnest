from itertools import combinations

my_list = ['H', 'Z', 'A', 'L', 'E']

list_combinations = list()

def my_combinations(my_list):
    for n in range(len(my_list**2) + 1):
        yield list(combinations(my_list, n))

for i in my_combinations(my_list):
    print(i)