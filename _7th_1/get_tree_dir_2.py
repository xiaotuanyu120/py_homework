#!/usr/bin/python
# coding=utf-8


'''get the path info and put it into a file'''

import os
import subprocess


def cmd(command):
    process = subprocess.Popen(
        args=command,
        stdout=subprocess.PIPE,
        shell=True
    )
    return process.communicate()[0]


if __name__ == '__main__':
    path = '/root/python/homework'
    cmdline = 'tree ' + path
    result = cmd(cmdline)

    os.system('rm -f filepath_info_2.txt')
    with open('filepath_info_2.txt', 'a') as f:
        f.write(result)
