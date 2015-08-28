'''Analysis the number of code lines and
annotation lines of *.py file in current folder
'''

import os
import re
import sys


def get_file_list(dir_path):
    file_result = []
    all_file = [x for x in os.listdir(dir_path) if os.path.isfile(x)]
    for f in all_file:
        fname, ext = os.path.splitext(f)
        if ext == '.py':
            file_result.append(f)
    return file_result


def get_analysis_info(fname):
    analysis_result = {"Annotation": 0, "Code": 0, "Total": 0, "Spaces": 0}
    with open(fname) as f:
        flag = [0]
        for line in f:
            if flag[0] == 0:
                if re.search('^\s*$', line):
                    analysis_result["Spaces"] += 1
                elif re.search(r'^\s*("""|\'\'\')', line):
                    if re.search(r'^\s*("""|\'\'\').*("""|\'\'\')$', line):
                        analysis_result["Annotation"] += 1
                    else:
                        flag[0] += 1
                elif re.search('\s+#', line):
                    analysis_result["Annotation"] += 1
                    if not re.search('^\s*#', line):
                        analysis_result["Code"] += 1
                else:
                    analysis_result["Code"] += 1
            elif re.search(r'^.*("""|\'\'\')\s*$', line):
                analysis_result["Annotation"] += flag[0] + 1
                flag[0] = 0
            else:
                flag[0] += 1
            analysis_result["Total"] += 1
    return analysis_result


def get_path():
    try:
        sys.argv[1]
    except IndexError as e:
        print "Error: you must assign a PATH!", e
        sys.exit(0)
    return sys.argv[1]


if __name__ == '__main__':
    dir_path = get_path()
    file_list = get_file_list(dir_path)
    for fname in file_list:
        a_result = get_analysis_info(fname).items()
        p_result = ['\t%10s : %-d' % (k, v) for k, v in a_result]
        print '\t----------------------------'
        print '\t%10s : %-s\n' % ('Filename', fname)
        for i in p_result:
            print i
