#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 
# software: PyCharm
# file: 4.thread_pool_usage.py
# Created by eason on 2018/4/4 13:19
# site: jinbitou.net
# contact: wang.eason2016@gmail.com
import threading
import time
from queue import Queue


def f(n):
    """
    需要多线程执行的目标函数
    :param n:
    :return:
    """
    print('我执行完需要{}秒钟'.format(n))
    time.sleep(n)


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.q = queue
        self.daemon = True  # 将线程声明为守护线程
        self.start()

    def run(self):
        while 1:
            # 从队列中删除并返回一个待执行任务
            f, args, kwargs = self.q.get()
            try:
                f(*args, **kwargs)  # 执行传进来的方法
            except Exception as e:
                print(e)
            self.q.task_done()


class ThreadPool(object):
    """
    保证同时thread_num个线程在工作
    """
    def __init__(self, thread_num=10):  # 默认10个线程
        self.q = Queue(thread_num)
        # 创建工作线程
        for i in range(thread_num):
            Worker(self.q)

    def add_task(self, f, *args, **kwargs):
        self.q.put((f, args, kwargs))  # 向队列中添加一个任务

    def wait_complete(self):
        self.q.join()  # 阻塞直到所有任务都被执行完毕


if __name__ == '__main__':
    start = time.time()
    pool = ThreadPool(5)  # 五个线程
    for i in range(10):  # 执行f方法10次
        pool.add_task(f, 3)  # 每次3秒
    pool.wait_complete()
    end = time.time()
    print('耗时:{}'.format(end-start))