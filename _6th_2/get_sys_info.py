#!/usr/bin/python

'''collect the sys info like cpu memory and network flow'''

import psutil


def get_sys_info():
    result = {
        'cpu_usage': psutil.cpu_percent(),
        'mem_usage': psutil.virtual_memory().percent,
        'net_in': psutil.net_io_counters().bytes_recv,
        'net_out': psutil.net_io_counters().bytes_sent
    }

    return result


if __name__ == '__main__':
    data = get_sys_info()
    with open('monitor_sys_info.log', 'a') as f:
        result = ["%s:%s" % (k, v) for k, v in data.items()]
        f.write('\t'.join(result)+"\n")
