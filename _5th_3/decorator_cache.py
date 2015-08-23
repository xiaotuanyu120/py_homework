#!/usr/bin/python


'''decorator and recurision'''

import time

def process_time(func):
    def inner(args):
        start = time.time()
        result = func(args)
        time_spent = time.time() - start
        print "\ttime spent is: %.4f" % time_spent
    return inner

def cache(func):
    cache_dic = dict()
    def inner(args):
        if args not in cache_dic:
            cache_dic.update({args:func(args)})
        else:
            print "\thit cache"
        print '\tthe result is: %d' % cache_dic[args]
        return cache_dic[args]
    return inner

@process_time
@cache
def multiple(number):
    result = 1
    for i in range(1, number):
        result = result * i
    return result

if __name__ == "__main__":
    while True:
        number = raw_input("input a number pls:")
        if number == 'quit':
            break
        try:
            number = int(number)
        except ValueError as e:
            print "pls input a number or quit"
            continue
        multiple(number)
