#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的
import os

word='hot'
dic=['doh', 'got'  , 'dot' , 'god' , 'tod'  , 'dog' , 'lot' , 'log']

def getone(start,i,end):
    print(start,end)
    if  panduan(start,end):
        return 'OK'     
    for x in dic:
        # ii=i
        print('x:==',x)
        if panduan(start,x):
            i+=1
            getone(x,i,end)
    pass


grap={}
def creategraph(start,li):
    tmp=[]
    for x in li:
        if panduan(start,x):
            if start==x:
                print('两个相等！')
                pass
            else:
                tmp.append(x)
    grap[start]=tmp


def panduan(start,x):
    # 判断是否可以变换
    s1=list(start)
    s2=list(x)
    same=0
    for x in range(len(s1)):
        if s1[x]==s2[x]:
            same+=1
    if same>1:
        return True
    return False

def getkv(key,end,xulie):
    print('key:',key,'|getkv: |xulie:',xulie)
    if (key not in xulie):
        # xulie.append(key)
        for value in grap[key]:
            if value==end:
                xulie.append(value)
                print('-----------OK----------',end)
                print(xulie)
                continue 
            else: 
                xulie.append(key)
                getkv(value,end,xulie)
            pass
    else:
        # print('循环图',xulie)
        xulie.pop()
        # break


def main():
    n = 5 #int(input()) 
    m=140 
    # li=[100 ,30, 20 ,110 ,120]
    li=[10 ,70, 20 ,90 ,50]
    # li=[10 ,30, 20 ,40 ,50]
    li.sort()

    print(li )
    # res=getone(word,0,word[::-1])
    # print(res)

if __name__ == '__main__':
    main()
# 生成无向图：
    end=word[::-1]
    dic.append(end)
    print(dic)
    creategraph(word,dic)
    for x in dic:
        creategraph(x,dic)
        pass
    print(grap)
    rr=[]
    getkv(word,end,rr)
    for x in grap.keys():
        for j in grap[x]:
            val=j
            pass
        pass

