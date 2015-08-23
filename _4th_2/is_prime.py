#!/usr/bin/python
#Filename:2907_if_prime.py
''' aim to check the number user give is prime or not'''

cache_prime = {}
while True:
    try:
        input_user = int(raw_input('Input a number : '))
    except ValueError:
        print 'what you input is not a number!'
        continue
    if input_user in cache_prime:
        print input_user, cache_prime[input_user]
        continue
    
    is_prime = False
    for i in range(2,input_user//2+1):
        if input_user % i == 0 and input_user != i:
            is_prime = False
            print "%d isn't prime" % input_user
            cache_prime[input_user] = "isn't prime"
            break
        else:
            print i
            is_prime = True
    if is_prime:
        print "%d is prime" % input_user
        cache_prime[input_user] = "is prime"
