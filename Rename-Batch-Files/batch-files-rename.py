# -*- coding: utf-8 -*-

# batch-files-rename.py
# 易凯创建于 21/02/2019
# 该程序将以批处理的方式在指定文件夹中所有指定后缀名的文件改成另一后缀名，然后将文件保存到上述指定文件夹

import os
import argparse

"""
该程序将以批处理的方式在指定文件夹中所有指定后缀名的文件改成另一后缀名，然后将文件保存到上述指定文件夹
work_dir: 指定文件夹
old_ext: 旧扩展名
new_ext: 新扩展名
"""
def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        # 得到文件扩展名
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 开始检查文件扩展名，如果 old_ext = file_ext：
        if old_ext == file_ext:
            # 返回更改文件扩展名的文件到指定文件夹
            newfile = split_file[0] + new_ext

            # 写入文件
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    return

def get_parser():
    parser = argparse.ArgumentParser(description='批处理改变制定文件夹下文件的扩展名')
    parser.add_argument('work_dir', metavar='WORK-DIR',type=str, nargs=1, help='将要改变文件扩展名的文件路径')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='旧扩展名')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='新扩展名')
    return parser

def main():
    """
    主函数在脚本被唤起时调用
    """
    # 添加命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())

    # 设置第一个传递的参数作为变量work_dir的实参
    work_dir = args['work_dir'][0]
    # 设置第二个传递的参数作为变量old_ext 的实参
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    # 设置第三个传递参数作为变量new_ext的实参
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)

if __name__ == '__main__':
    main()