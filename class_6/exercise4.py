
def manytimes(n):
    def howmany(func):
        def inner(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return inner
    return howmany
    return manytimes


@manytimes(3)
def my_function():
    print("Hello, world!")

my_function()