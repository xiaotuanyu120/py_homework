#!/usr/bin/python
# coding=utf-8


'''aim to analysis nginx access log, print request times each clock'''


def request_each_clock(filein):
    list_scan = []
    with open(filein) as f:
        for line in f:
            clock = line.split(':')[1]
            list_scan.append(clock)
    
    clock_dereplication = set(list_scan)
    clock_count = []
    for i in clock_dereplication:
        clock_count.append([i,list_scan.count(i)])

    clock_count.sort()
    return clock_count


## PATH OF INPUT FILE
path_log = '/root/py/05_2/access.log'

## COUNT REQUEST EACH CLOCK, RETURN A LIST
clock_times = request_each_clock(path_log)

## PRINT RESULT
format_str = '%-20s %s'
print format_str %('CLOCK','TIMES')
for i in range(len(clock_times)):
    print format_str %(clock_times[i][0],clock_times[i][1])
