'''Analysis the number of code lines and
annotation lines of *.py file in current folder
'''

import argparse
from os import path, listdir
from termcolor import colored

parser = argparse.ArgumentParser(description='statistics the code file')
parser.add_argument(
    '-p', '--path', default='.', dest='dirpath',
    help='set the path of the code file you want to statistic')
parser.add_argument(
    '-d', '--depth', default=1, dest='depth', type=int,
    help='the depth of the root path you want to statistic')


# ===================================================
# collect all python file in dir_path and it's subdir
# ===================================================
def get_file_list(dir_path, depth_path):
    file_result = []

    def inner_get_list(_dir_path, _depth_path):
        if _depth_path < 1:
            return None

        for x in listdir(_dir_path):
            fpath = path.join(_dir_path, x)
            fname, ext = path.splitext(fpath)
            if path.isfile(fpath) and ext == '.py':
                file_result.append(fpath)
            elif path.isdir(fpath):
                inner_get_list(fpath, _depth_path-1)

    inner_get_list(dir_path, depth_path)
    return file_result


# ==========================================
# parse file and return the result in dict
# ==========================================
def parse_file(file_name):
    Annotation = 0
    Code = 0
    Total = 0
    Spaces = 0

    with open(file_name) as f:
        multi_flag = 0
        multi_str_switch = False
        for line in f:
            line = line.strip()
            if multi_flag == 0:
                if line == '':
                    Spaces += 1
                elif '"""' in line or "'''" in line:
                    if multi_str_switch:
                        multi_str_switch = False
                        Code += 1
                    else:
                        if is_multi_comment_start(line):
                            multi_flag += 1
                        else:
                            multi_str_switch = True
                            Code += 1
                elif is_comment(line):
                    Annotation += 1
                elif is_end_comment(line):
                    Annotation += 1
                    Code += 1
                else:
                    Code += 1
            elif is_multi_comment_end(line):
                Annotation += multi_flag + 1
                multi_flag = 0
            else:
                multi_flag += 1
            Total += 1

    parse_result = [Code, Annotation, Spaces, Total]
    return parse_result


# ======================================
# judge a code line is annotation or not
# ======================================
def is_comment(line):
    if line.startswith('#'):
        return True
    elif line.startswith('"""') and line.endswith('"""') and len(line) >= 6:
        return True
    elif line.startswith("'''") and line.endswith("'''") and len(line) >= 6:
        return True
    else:
        return False


# ================================================
# judge code line is multi annotation start or not
# ================================================
def is_multi_comment_start(line):
    if line.startswith('"""') or line.startswith("'''"):
        if len(line) >= 6 and line.endswith('"""') or line.endswith("'''"):
            return False
        else:
            return True
    else:
        return False


# ==============================================
# judge code line is multi annotation end or not
# ==============================================
def is_multi_comment_end(line):
    if line.endswith('"""') or line.endswith("'''"):
        return True
    else:
        return False


# =======================================
# judge code line have end comment or not
# =======================================
def is_end_comment(line):
    if '#' in line and not line.startswith('#'):
        line = line.rsplit('#')[0]
        if line.count('"') % 2 != 0 or line.count("'") % 2 != 0:
            return False
        else:
            return True


def main():
    args = parser.parse_args()

    file_list = get_file_list(args.dirpath, args.depth)
    for fname in file_list:
        content = parse_file(fname)
        title = ['Code line', 'Annotation', 'Spaces', 'Total']
        color = ['red', 'yellow', 'blue', 'green']
        result = zip(title, content, color)

        print '----------------------------'
        print colored(''.join(['Filename : ', fname]), 'cyan')
        for i in range(len(result)):
            format = ''.join([result[i][0], ':', str(result[i][1])])
            print colored(format, result[i][2])


if __name__ == '__main__':
    main()
