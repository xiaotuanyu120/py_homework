#!/usr/bin/python
# coding=utf-8


'''aim to analysis nginx access log, print request times each file type'''


def filetype_count(filein):
    list_scan = []
    with open(filein) as f:
        for line in f:
            filetype = line.split('"')[1].split()[1]
            list_scan.append(filetype)
    
    filetype_dereplication = ['.js', '.css', '.html', '.png']
    filetype_count = []
    percent_div = len(list_scan)
    for i in filetype_dereplication:
        count_i = 0
        for j in list_scan:
            if i in j:
                count_i += 1
        percentage = float(count_i)*100/percent_div
        filetype_count.append([i,percentage])
    return filetype_count

## PATH OF INPUT FILE
path_log = '/root/py/05_2/access.log'

## COUNT REQUEST EACH FILETYPE, RETURN A LIST
filetype_times = filetype_count(path_log)

## PRINT RESULT
print '%-20s %s' %('FILETYPE','PERCENTAGE')
for i in range(len(filetype_times)):
    print '%-20s %.2f' %(filetype_times[i][0],filetype_times[i][1])
