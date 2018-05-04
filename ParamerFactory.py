#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import numpy as np
import ParamerManager as pm
import random

#汇水面各个参数的范围
subAreaParaRange = [[0.005, 0.05], [0.005, 0.5], [0.2, 10], [2, 10], [5, 85], [25, 80], [0, 10], [2, 7]]
#曼宁系数范围
manningRange = [0.011, 0.024]
#淤积占最大深度的比例
persentOfMax = 0.3

'''
产生一组汇水面参数
'''
def subAreaParamer():
    global subAreaParaRange
    s = []
    for prange in subAreaParaRange:
        s.append(round(random.uniform(prange[0], prange[1]), 2))
    return s

'''
产生一个曼宁系数
'''
def manningParamer():
    global manningRange
    return round(random.uniform(manningRange[0], manningRange[1]), 3)

'''
产生一个管道淤积参数，maxN为管道高度，默认1m
'''
def pipParamer(maxN=1):
    global persentOfMax
    a = random.random() * maxN * persentOfMax
    return round(a, 5)  # 保留5位小数

'''
产生一组数据，【汇水面参数，曼宁系数，淤积高度】
'''
def getOneGroupParamer():
    group = subAreaParamer()
    group.append(manningParamer())
    group.append(pipParamer())
    return group


if __name__ == "__main__":
    print(getOneGroupParamer())
