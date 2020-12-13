"""
@File   : test.py
@Author : wangzhixiang
@Time   : 2020/12/9 21:50
"""
import time
from multiprocessing import Pool


def read_file(i):
    f = open(r'D:\workspace2020\jike_alg\a.txt', 'a')
    print(id(f))
    f.write(str(i) * (1000000000 - i))
    print(id(f))
    time.sleep(5)


if __name__ == '__main__':
    # with Pool(3) as pool:
    #     pool.map(read_file, range(3))
    f = open(r'D:\workspace2020\jike_alg\a.txt', 'r')
    data = f.read()
    print(len(data))
    print(data[999999990:1000000000])
    print(data[1999999990:])

