#!/usr/bin/python


'''decorator and recurision'''

def cache(func):
    cache_dic = dict()
    def inner(args):
        if args not in cache_dic:
            cache_dic.update({args:func(args)})
        else:
            print '\thit cache'
        return cache_dic[args]
    return inner

def count(func):
    def inner(new_n):
        global count_fib
        count_fib += 1
        result = func(new_n)
        return result
    return inner

@count
@cache
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    while True:
        number = raw_input("input a number pls:")
        if number == 'quit':
            break
        try:
            number = int(number)
        except ValueError as e:
            print e
        count_fib = 0
        print "\t============================\n\tthe %dth fib is %r" %(number, fib(number))
        print "\tthe process times is %d" % count_fib
