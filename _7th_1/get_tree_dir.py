#!/usr/bin/python


'''get the path info and put it into a file'''

import glob
from os import walk, system


def path_structure(path):
    result = {}
    for dirname, subdirs, filenames in walk(path):
        result[dirname] = filenames
        result[dirname].extend(subdirs)
        for subdir in subdirs:
            if not glob.glob(path+subdir) == []:
                result[subdir] = glob.glob(path+subdir)
    return result


if __name__ == '__main__':
    path = "/root/python/homework"
    data = path_structure(path).items()
    data = sorted(data, cmp=lambda x, y: cmp(len(x[0]), len(y[0])))
    import ipdb;ipdb.set_trace()
    system('rm -f filepath_info.txt')
    with open('filepath_info.txt', 'a') as f:
        f.write('/root/python/homework\n')
        for i in range(len(data)):
            f.write('\t|-- %s\n' % data[i][0])
            for j in range(len(data[i][1])):
                f.write('\t|\t|-- %s\n' % data[i][1][j])
