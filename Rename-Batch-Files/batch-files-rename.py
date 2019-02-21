# -*- coding: utf-8 -*-

# batch-files-rename.py
# 易凯创建于 21/02/2019
# 该程序将以批处理的方式在指定文件夹中所有指定后缀名的文件改成另一后缀名，然后将文件保存到上述指定文件夹

import os
import argparse

"""
Batch rename a group of files in a given directory.
work_dir: the given directory
old_ext: name of old extension
new_ext: name of new extension
"""
def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        # Get the file extension
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        if old_ext == file_ext:
            # Returns changed name of the file with new extension
            newfile = split_file[0] + new_ext

            # Write the files -- 此处后续进行分析
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    return

# def get_parser():
#     parser = argparse.ArgumentParser(description='批处理改变制定文件夹下文件的扩展名')
#     parser.add_argument('work_dir', metavar='WORK-DIR',type=str, nargs=1, help='将要改变文件扩展名的文件路径')
#     p

def main():
    """
    主函数在脚本被唤起时调用
    """
    # 添加命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())

    # 设置变量 work_dir 作为第一个传递的参数
    work_dir = args