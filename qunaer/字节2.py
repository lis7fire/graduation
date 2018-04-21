#!/usr/bin/python3
#coding: utf-8
import sys

def getT(num,li):
    print('gesu为：',num)
    print('周期为：',li)
    pass


def main():
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        # print(line)
        values = list(map(int, line.split()))
        # print('values:',values[1:])
        # for v in values:
        #     ans += v
        num=values[0]
        getT(num,values[1:])
    print('end')

if __name__ == '__main__':
    main()