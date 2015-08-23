#!/usr/bin/python


'''same to map()'''

def inside(func, iterable):
    try:
       callable(func)
    except NameError as e:
       print e
    for i in range(len(iterable)):
        iterable[i] = func(iterable[i])
    return iterable

if __name__ == 'main':
    inside()
