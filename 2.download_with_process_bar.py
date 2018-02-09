#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
__author__ = "eason"
import requests
import os
from tqdm import tqdm


def download_file(url: str, save_path: str)->bool:
    """
    下载文件并显示下载进度
    :param url: 文件url
    :param save_path: 保存路径
    :return:
    """
    try:
        local_filename = os.path.join(save_path, url.split('/')[-1])
        r = requests.get(url, stream=True, timeout=60)
        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0))
        # print url, total_size
        with open(local_filename, 'wb') as f:
            for chunk in tqdm(r.iter_content(), total=total_size, unit='B', unit_scale=True, desc=url.split('/')[-1],
                              leave=True, ncols=100):
                f.write(chunk)
        return True
    except Exception as e:
        print(repr(e))
        return False

if __name__ == "__main__":
    download_file(url="https://dldir1.qq.com/qqfile/qq/TIM2.1.0/22747/TIM2.1.0.exe", save_path=r"C:\Users\eason\Desktop\test")