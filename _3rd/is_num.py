#!/usr/bin/python
#Filename:is_num.py
''' aim to check user's input, if num yes, else no, retry pls. '''

while True:
    try:
        input_user = int(raw_input('Input a number : '))
        print 'the number is %d'% input_user
        break
    except ValueError:
        print 'what you input is not a number!'
else:
    print 'Done'

