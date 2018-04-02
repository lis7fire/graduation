#!/usr/bin/python3
# coding: utf-8
# 上面两句注释必须要，防止无法打印中文的
import os

word='hot'
dic=['doh', 'got'  , 'dot' , 'god' , 'tod'  , 'dog' , 'lot' , 'log']

def creategraph(start,li):    
    # grap={}
    tmp=[]
    for x in li:
        if panduan(start,x):
            if start==x:
                # print('两个相等！')
                pass
            else:
                tmp.append(x)
    # grap[start]=tmp
    return tmp

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

def getkv(grap,key,end,xulie):
    print('key:',key,'|getkv: |xulie:',xulie)
    if (key not in xulie):
        # xulie.append(key)
        for value in grap[key]:
            if value==end:
                xulie+=[value]
                print('-----------OK----------',end)
                print(xulie)
                return xulie 
            else: 
                xulie+=[key]
                aaa=getkv(grap,value,end,xulie)
            pass
    else:
        print('循环图',xulie)
        xulie.pop()
        # break

def find_path(graph, start, end, path=[]): #查找任意一条路径
        path = path + [start] #先把起始节点加入
        if start == end:
            print('找到了：',path)
            return path
        if  graph.get(start,0)==0: #没有这个节点的key
            print('最后一个节点',xulie)
            return None
        for node in graph[start]:
            if (node not in path): #如果不在路径之内
                newpath = find_path(graph, node, end, path)
                print('newpath:',newpath)
                if newpath:
                    return newpath
        return None

def find_all_paths(graph, start, end, path=[]): #查找所有路径
    path = path + [start]
    if start == end:
        return [path]
    if graph.get(start,0)==0:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

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
    # dic.append(word)
    dic.append(end)
    print(dic)
    grap={}
    grap[word]=creategraph(word,dic)
    for x in dic:
        grap[x]=creategraph(x,dic)
        pass
    print(grap)
    print('---------------------')
    rr=[]
    getkv(grap,word,end,rr)
    for x in grap.keys():
        for j in grap[x]:
            val=j
            pass
        pass
    aa=find_path(grap,word,end)
    print(aa)
    bb=find_all_paths(grap,word,end)
    print(bb)
