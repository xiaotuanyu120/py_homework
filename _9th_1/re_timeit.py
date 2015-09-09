#!/usr/bin/python

'''Aim to test which statement is faster between re.compile and
match directly'''

import timeit
import re


def re_c_test():
    s = ['good', 'hello', 'hub', 'hock', 'hong']
    t = re.compile('he')
    for i in s:
        t.match(i)


def re_m_test():
    s = ['good', 'hello', 'hub', 'hock', 'hong']
    for i in s:
        re.match("he", i)


if __name__ == "__main__":
    n = 1000000

    re_c = timeit.Timer("re_c_test()", "from __main__ import re_c_test")
    re_m = timeit.Timer("re_m_test()", "from __main__ import re_m_test")

    re_c_time = re_c.repeat(3, n)
    re_m_time = re_m.repeat(3, n)

    print 're_m run %d times cost\n\t%r' % (n, re_m_time)
    print 're_c run %d times cost\n\t%r' % (n, re_c_time)
