from functools import wraps

def my_decorator(func):
    #@wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say():
    '''here describe this function'''
    print "hello, called say() function"
