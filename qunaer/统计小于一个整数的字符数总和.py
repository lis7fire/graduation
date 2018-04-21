#!/usr/bin/python3
#coding: utf-8
import sys

outli=[]
def coun(n,leng):
    if leng==1:
        xx= n
        pass
    else:
        summ=digui(leng-1)
        print('summ',summ)
        xx=summ +((n-10**(leng-1))+1)*leng
    global outli
    outli.append(xx)
    pass

def digui(num):
    s=0
    if num==1:
        return 9
        pass
    else:
        s=9*(10**(num-1))*num+digui(num-1)
    return s

def out(outlist):
    for x in outlist:
        print(x)

def main():
    # 读取第一行的n
    # T = int(sys.stdin.readline().strip())
    T=3
    for i in (9,100,15510):#range(T)
        # n = sys.stdin.readline().strip()
        n=i
        leng=len(str(n))  
        # print('changdu:',leng)
        coun(n,leng)
        # getT(num,values[1:])
    global outli
    print('outli',outli)
    out(outli)

if __name__ == '__main__':
    main()