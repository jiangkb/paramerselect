#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import numpy as np
import ParamerManager as pm
import random

subAreaParaRange = [[0.005, 0.05], [0.005, 0.5], [0.2, 10], [2, 10], [5, 85], [25, 80], [0, 10], [2, 7]]
persentOfMax = 0.1


def subAreaParamer():
    global subAreaParaRange
    s = []
    for prange in subAreaParaRange:
        s.append(round(random.uniform(prange[0], prange[1]), 2))
    return s


def pipParamer(maxN):
    global persentOfMax
    s = []
    a = random.random() * maxN * persentOfMax
    s.append(maxN)
    s.append(round(a, 5))  # 保留5位小数
    return s


if __name__ == "__main__":
    value=subAreaParamer()
    pm.changeSubArea8('S1', value)
    print(value)
    print(pipParamer(4))
