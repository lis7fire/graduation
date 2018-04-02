#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的
import time  
import datetime
import os

word=['hot']
dic=['doh', 'got'  , 'dot' , 'god' , 'tod'  , 'dog' , 'lot' , 'log']


w = ['hot']
dic = ['doh', 'got', 'dot', 'god', 'tod', 'dog', 'lot', 'log']


def result(n,m,li):
    length=len(li)
    i=n-2
    j=n-1
    while j>0:
        sum1=li[j]
        while i>=0:
            if (li[i]+sum1)>m :
                i-=1
            elif (li[i]+sum1)==m:
                return 'prefect'
            else:
                sum1+=li[i]
                i-=1
        j-=1
        print(sum1)
    return 'good'

def main():
    n = 5 #int(input()) 
    m=140 
    # li=[100 ,30, 20 ,110 ,120]
    li=[10 ,70, 20 ,90 ,50]
    # li=[10 ,30, 20 ,40 ,50]
    li.sort()

    print(li )
    res=result(n,m,li)
    print(res)


if __name__ == '__main__':
    main()