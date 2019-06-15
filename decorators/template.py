# This is the template for writing decorators
import functools

def decorator(func): # receive the func to be decorated
    @functools.wraps(func) # without this wrapper, we can't see the decorated function original specs, we can only see the properties of the decorator's properties
    def wrapper_decorator(*args, **kwargs): # the function used to decorate the func and return this function as the decorated function
        # *args, **kwargs are used to receive original arguments from the func
        #Do something before <the decorating things>
        value = func(*args, **kwargs) # and process the original arguments
        #Do something after <the decorating things>
        return value # and return the processed value to the decorated function
    return wrapper_decorator # return the decorated function
# such that we can do three things here:
# 1. decorators can receiver arguments(using *args and **kwargs) from the original func, and use func to process them
# 2. decorated function can return value which is the result the func processed
# 3. return the decorated function back as the decorated function of func
# 4. use functools.wraps to show the original func properties instead of the decorated function
