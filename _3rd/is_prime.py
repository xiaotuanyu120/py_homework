me:2907_if_prime.py
''' aim to find all prime from 0 to the number user give. '''

while True:
    try:
        input_user = int(raw_input('Input a number : '))
        print '==========start========'
        num_div = input_user // 2 + 1
        for num_find in range(2,input_user + 1):
            count_div = 0
            for i in range(2,num_div):
                result_div = float(num_find) / i
                result_div_int = num_find / i
                #print "num:",num_find,'-',i,'-',result_div,'-',result_div_int
                if result_div == result_div_int and num_find != i:
                    count_div = 0
                    continue
                else:
                    count_div += 1
                #print count_div
            if len(range(2,num_div)) == count_div:
                print "prime : %d" % num_find
        break
    except ValueError:
        print 'what you input is not a number!'
print '==========Done========'

