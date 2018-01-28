# -*- coding: utf-8 -*-
__author__ = "eason"
import os


def get_file_by_suffix(folder: str, suffix: str = None, deep: int = None)->str:
    """
    生成器函数，返还给定目录中指定格式的文件路径
    :param folder: 要遍历的根目录
    :param suffix: 要查找的指定格式，小写，如果有多种格式用逗号隔开，例如"pdf,zip,rar"
    :param deep: 查找深度，默认全部查找，0为当前目录
    :return:
    """
    for parent, dirnames, filenames in os.walk(folder):
        # print("当前目录：", parent)
        # print("下层文件夹名字：", dirnames)
        for filename in filenames:
            file_location = os.path.join(parent, filename)
            # print("相对深度：", parent.count("\\")-folder.count("\\"))
            if suffix:
                match_list = suffix.split(",")
                for suffix in match_list:
                    if deep is not None:
                        if (parent.count("\\")-folder.count("\\")) <= deep and file_location.endswith(suffix):
                            yield file_location
                        else:
                            pass
                    elif file_location.endswith(suffix):
                            yield file_location
                    else:
                        pass
            elif deep is not None:
                if (parent.count("\\") - folder.count("\\")) <= deep:
                    yield file_location
            else:
                yield file_location


if __name__ == "__main__":
    for file in get_file_by_suffix(folder=r"C:\Users\eason\Desktop\test", suffix="xls,xlsx"):
        print(file)