#!/usr/bin/python3
#coding: utf-8
import sys

s=['u', 'u', 'u', 'r', 'r', 'd', 'd', 'd', 'd', 'd', 'l']
num=3

outli=[]

def getlen(ss,n,m,x,y):
    print(ss,n,m,x,y)
    step=0
    gameover=False
    global outli
    for i in ss:
        if i=='u':
            x=x-1
            step+=1
            gameover=over(n,m,x,y)
        elif i=='d':
            x=x+1
            step+=1
            gameover=over(n,m,x,y)
        elif i=='l' :
            y=y-1
            step+=1
            gameover=over(n,m,x,y)
        else:
            y=y+1
            step+=1
            gameover=over(n,m,x,y)
            pass
        if gameover:
            print('游戏提前结束')
            return step
            pass
    return step
    pass


def over(n,m,x,y):
    if x>n or x<1:
        return True
    if y>m or y<1:
        return True
    return False
    pass

def out(outlist):
    for x in outlist:
        print(x)

def main():
    sss = ['u', 'u',  'r', 'u', 'r', 'u',  'u', 'r', 'u', 'r','r', 'u', 'r', 'u',  'u', 'r', 'u', 'r','r', 'u', 'r', 'u',  'u', 'r', 'u', 'r','r', 'u', 'r', 'u',  'u', 'r', 'u', 'r', 'r', 'd', 'd', 'd', 'l']
    # 读取第一行的n
    n = 3
    for i in range(n):
        # 读取每一行
        values = [1666,2938,100,200]
        n=values[0]
        m=values[1]
        x=values[2]
        y=values[3]
        outli.append(getlen(sss,n,m,x,y))
    # global outli
    out(outli)

if __name__ == '__main__':
    main()