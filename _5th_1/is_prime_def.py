#!/usr/bin/python
#Filename:is_prime_def.py
''' aim to find all prime from 0 to the number user give. '''
def is_num(x):
    try:
        int(x)
        return 1
    except ValueError:
        return 0

def is_prime(y):
    if is_num(y):
        y = int(y)
        if y > 1:
            for i in range(2,y//2+1):
                if y % i == 0:
                    return 0
                    break
                else:
                    return 1
        else:
            print "number must bigger than 1!"
    else:
        print "you must input a number!"

while True:
    input_user = raw_input('Input a number :').strip()
    if is_num(input_user):
        input_user = int(input_user)
    else:
        print 'you must input a number'
        continue

    print '==========start========'
    for num_prime in range(2,input_user + 1):
        if is_prime(num_prime):
            print "prime : %d" % num_prime
    break
print '==========Done========'
