#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的
import time  
import datetime
import os
from pyquery import PyQuery as pq
import pymysql.cursors
import json

start = datetime.datetime.now()
# start = round(time.time()*1000)  
print(start)
print('Done！！！')
a=[1,2,3,4]
b=[7,8,9,0]
for x in a+b:
	print(x)

end = datetime.datetime.now()
print(end)
print("插入数据库消耗时间：Cast: ",(end-start).microseconds/1000,"ms")

class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        sum=0
        for x in nums[::2]  :
            sum+=x
        return sum
print(Solution().arrayPairSum([1,4,3,2,6,5]))

def init_errno():
    with open('./canshu.json','r',encoding='utf-8') as jsfile:
        errno=json.load(jsfile)
    print(errno)
    print('---')

init_errno()

dir='/2014Sony'
a=dir.split('/')
print(len(a)==2)
print(dir.rstrip(a[-1]).rstrip('/'))

a=[0,1,2,3]
b=[4,5,6,7]
c=[8,9,'a','b']
d=['c','d','e','f']
aa=[]
aa.append(a)
aa.append(b)
aa.append(c)
aa.append(d)
print(aa)