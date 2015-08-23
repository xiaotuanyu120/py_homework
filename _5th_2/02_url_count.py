#!/usr/bin/python
# coding=utf-8


'''aim to analysis nginx access log, print request time top 100.'''


def url_count(filein):
    list_scan = []
    with open(filein) as f:
        for line in f:
            url = line.split()[6].split('?')[0]
            list_scan.append(url)
    
    list_dereplication = set(list_scan)
    url_count = []
    for i in list_dereplication:
        url_count.append([i,list_scan.count(i)])

    url_count.sort(key=lambda x:x[1],reverse=True)
    return url_count


## PATH OF INPUT FILE
path_log = '/root/py/05_2/access.log'

## COUNT URL , RETURN A LIST
url_times = url_count(path_log)

## PRINT RESULT
format_str = '%-70s %s'
print format_str %('URL','TIMES')
for i in range(50):
    print format_str %(url_times[i][0],url_times[i][1])
