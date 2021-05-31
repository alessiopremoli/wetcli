
import os, math, bitmath
from posixpath import join

excluded_files = ['.DS_Store', ]


def sanitize_and_check_files(files):
    print('Cheking files...')

    if len(files) == 0:
        raise Exception('No files provided!')

    s_files = [f'test_files/{file}' for file in files if file not in excluded_files]

    if len(s_files) > len(set(s_files)):
        raise Exception('Duplicate files found!')

    dirname = os.path.dirname(__file__)
    total_size = sum([os.path.getsize(os.path.join(dirname, f'../{file}')) for file in s_files])

    if bitmath.Byte(total_size) > bitmath.GiB(2).to_Byte():
        raise Exception('Files too big!')

    print('Files OK!')

    return s_files