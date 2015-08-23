#!/usr/bin/python
# coding=utf-8


'''aim to analysis nginx access log, print request time top 100.'''

def file_scan(filein):
    list_f = []
    with open(filein) as f:
        f.seek(0)
        for line in f:
            url = line.split()[6].split('?')[0]
            request_time = line.split('"')[9]
            list_f.append([url,request_time])
    list_f = sorted(list_f,key=lambda x:float(x[1]),reverse=True)
    return list_f

## PATH OF INPUT FILE
path_log = '/root/py/05_2/access.log'

## CONVERT LOG FILE TO LIST
file_dict = file_scan(path_log)

## PRINT RESULT
format_str = '%-45s %s'
print format_str %('URL','REQUEST TIME')
for i in range(100):
    print format_str %(file_dict[i][0],file_dict[i][1])
