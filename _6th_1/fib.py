#!/usr/bin/python


'''recurision'''

from fib_cache import *

#@count
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
        #count_fib = [0]
        print "\t============================\n\tthe %dth fib is %r" %(number, fib(number))
        #print "process times is %d" %count_fib[0]
