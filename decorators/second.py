def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def hello(name):
    print("hello %s" % name )
    return name

p = hello("lin")
print(p)
