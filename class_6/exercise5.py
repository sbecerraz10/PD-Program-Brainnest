def decorator(func):
    def inner1(*args, **kwargs):
        print(f"the value of args{args} and kwrgs{kwargs} ")
        returned_value = func(*args, **kwargs)
        return returned_value
        
    return inner1

@decorator
def sum_two_numbers(a, b):
    return a + b

print(f"The sum is: {sum_two_numbers(9,18)}")