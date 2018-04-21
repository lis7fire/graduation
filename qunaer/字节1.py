#!/usr/bin/python3
#coding=utf-8
import sys

word=['hot']
dic=['doh', 'got'  , 'dot' , 'god' , 'tod'  , 'dog' , 'lot' , 'log']


w = ['hot']
dic = ['doh', 'got', 'dot', 'god', 'tod', 'dog', 'lot', 'log']
outli=[]
def getT(num,li):
    print('gesu为：',num)
    print('周期为：',li)
    xmax=li[num-1]-li[0]
    xmin=li[1]-li[0]
    for a in range(num):
        pass
    print(xmin)
    outli.append(xmin)
    pass

def out(outlist):
    for x in outlist:
        print(x)
    

def main():
    num=3
    li=[2,4,6]
    getT(num,li)


if __name__ == '__main__':
    main()