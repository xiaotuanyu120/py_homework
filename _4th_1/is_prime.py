#!/usr/bin/python
#Filename:2907_if_prime.py
''' aim to find all prime from 0 to the number user give. '''

while True:

    try:
        input_user = int(raw_input('Input a number : '))
    except ValueError:
        print 'what you input is not a number!'
        continue

    print '==========start========'
    num_div = input_user // 2 + 1
    for num_find in range(2,input_user + 1):
        is_prime = False
        for i in range(2,num_div):
            if num_find % i == 0 and num_find != i:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            print "prime : %d" % num_find
    break
print '==========Done========'

