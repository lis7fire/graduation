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


def result(word, dict):
    #revchars = word[::-1]
    # alist = revchars.split('')
    revchars = list(word)
    print(revchars)


def main():
    dic = []
    word = 'hot'#input()
    list1 = 'doh got dot god tod dog lot log' #input()
    if list1 != "":
        for x in list1.split():
            # print(list(x))
            dic.append(list(x))
    print('dic',dic)
    result(word, dic)


if __name__ == '__main__':
    main()