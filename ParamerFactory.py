#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import numpy as np
import ParamerManager as pm
import random

subAreaParaRange = [[0.005, 0.05], [0.005, 0.5], [0.2, 10], [2, 10], [5, 85], [25, 80], [0, 10], [2, 7]]
manningRange = [0.011, 0.024]
persentOfMax = 0.3


def subAreaParamer():
    global subAreaParaRange
    s = []
    for prange in subAreaParaRange:
        s.append(round(random.uniform(prange[0], prange[1]), 2))
    return s


def manningParamer():
    global manningRange
    return round(random.uniform(manningRange[0], manningRange[1]), 3)


def pipParamer(maxN=1):
    global persentOfMax
    a = random.random() * maxN * persentOfMax
    return round(a, 5)  # 保留5位小数


def getOneGroupParamer():
    group = subAreaParamer()
    group.append(manningParamer())
    group.append(pipParamer())
    return group


if __name__ == "__main__":
    print(getOneGroupParamer())
