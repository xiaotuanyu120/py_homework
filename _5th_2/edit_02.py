#!/usr/bin/python
# coding=utf-8


'''aim to analysis nginx access log, print the result'''


def split_to_list(filein,separator=' ',index=0):
    '''split file by separator and collect data which the index directed into a list'''
    list_scan = []
    with open(filein) as f:
        for line in f:
            element = line.split(separator)[index]
            list_scan.append(element)
    return list_scan
    
def count_to_list(count_data,source_data):
    '''count_data is the list used in for loop; source_data is the list where counted from'''
    count_list = []
    for i in count_data:
        count_list.append([i,source_data.count(i)])
    count_list.sort()
    return count_list

def print_result(source_list,print_format,print_title,length=None):
    length = len(source_list) if not length else length
    print print_format %print_title
    for j in range(length):
        print format_str %(source_list[j][0],source_list[j][1])


## PATH OF INPUT FILE
path_log = '/root/py/05_2/access.log'

## select which question
print '''1: Top 100 of highest request time to url
2: Top 50 of most requested url
3: Count request times each clock
4: Count filetype requested percentage
======================================'''
while True:
    select = (raw_input('which question you want to select? ("1","2","3" or "4":)').strip())
    if select == '1':
        ## QUESTION 1
        ## CONVERT LOG FILE TO LIST
        url = split_to_list(path_log,index=6)
        request_time = split_to_list(path_log,separator='"',index=9)
        url_request_time = []
        for x in range(len(url)):
            url_request_time.append([url[x],request_time[x]])
        url_request_time = sorted(url_request_time,key=lambda x:float(x[1]),reverse=True)
        
        ## PRINT RESULT
        format_str = '%-45s %s'
        title_str = ('URL','REQUEST TIME')
        print_result(url_request_time,format_str,title_str,length=100)
        break
       
    elif select == '2':
        ## QUESTION 2
        ## COUNT URL , RETURN A LIST
        url_split = split_to_list(path_log,index=6)
        url_dereplication = set(url_split)
        url_times = count_to_list(url_dereplication,url_split)
        url_times = sorted(url_times,key=lambda x:float(x[1]),reverse=True)
        
        ## PRINT RESULT
        format_str = '%-60s %s'
        title_str = ('URL','TIMES')
        print_result(url_times,format_str,title_str,length=50)
        break

    elif select == '3':
        ## QUESTION 3
        ## COUNT REQUEST EACH CLOCK, RETURN A LIST
        clock_split = split_to_list(path_log,separator=":",index=1)
        clock_dereplication = set(clock_split)
        clock_times = count_to_list(clock_dereplication,clock_split)
        
        ## PRINT RESULT
        format_str = '%-20s %s'
        title_str = ('CLOCK','TIMES')
        print_result(clock_times,format_str,title_str)
        break

    elif select == '4':
        ## QUESTION 4    
        ## COUNT REQUEST EACH FILETYPE, RETURN A LIST
        filetype_split = split_to_list(path_log,separator='"',index=1)
        filetype = ['.js', '.css', '.html', '.png']
        filetype_count = []
        percent_div = len(filetype_split)
        for i in filetype:
            count_i = 0
            for j in filetype_split:
                if i in j:
                    count_i += 1
            percentage = float(count_i)*100/percent_div
            filetype_count.append([i,percentage])
        
        ## PRINT RESULT
        print '%-20s %s' % ('FILETYPE','PERCENTAGE')
        for i in range(len(filetype_count)):
            print '%-20s %.2f' %(filetype_count[i][0],filetype_count[i][1])
        break

    else:
        print "you must select a question in the list before!"
