#!/usr/bin/python


'''decorator'''

__all__ = ["cache"]

def cache(func):
    cache_dic = dict()
    def inner(args):
        if args not in cache_dic:
            cache_dic[args] = func(args)
        else:
            print '\thit cache'
        return cache_dic[args]
    return inner
'''
def count(func):
    count_fib = [0]
    def inner(new_n):
        count_fib[0] += 1
        result = func(new_n)
        return result
    return inner
'''
