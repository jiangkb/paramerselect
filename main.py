#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from pyswmm import Simulation
import numpy as np
import ParamerFactory as pf
import ParamerManager as pm
import sys as args

SubareaPm = []
PipPm = []
groupPm = []

'''
修改汇水面及管道淤积参数
'''


def modifyInp():
    global PipPm
    global SubareaPm
    PipPm = modifyPip()
    SubareaPm = modifysubArea()
    pm.saveFile()


'''
替换掉汇水面参数
'''


def modifysubArea(areas=7):
    subareas = []
    for i in range(areas):
        subareas.append(pf.subAreaParamer())
    pm.repliceAreas('S', subareas)
    return subareas


'''
获取管的醉倒高度并根据最大高度生成随机淤积，在替换inp
!!!!!!!!!!未保存INP，替换后需要手动保存pm.saveFile()！！！！！！！！！！！！
'''


def modifyPip(pips=11):
    maxArr = pm.getMaxGeom('C', pips)
    pip11 = []
    for i in maxArr:
        pip11.append(pf.pipParamer(i))
    pm.repliceGeom('C', pip11)
    return pip11


'''
运行swmm
'''


def runModel(path='example2\\Example.inp'):
    sim = Simulation(path)
    sim.execute()
    sim.close()


'''
计算结果中点pointName，与传入值的距离
'''


def computeDelta(pointName, avg, mas, maxt):
    avgSW, maxSW, maxTSW = pm.getResult3(pointName)
    maxTSW = maxTSW.split(':')
    # print(maxTSW)
    maxTNum = int(maxTSW[0]) * 60 + int(maxTSW[1])
    delta = abs(avg - avgSW) + abs(mas - maxSW) + abs(maxTNum - maxt)
    return delta


'''
通过一组参数，跟新汇水面，管道参数。
其中所有汇水面参数一样，所有管道参数一样
'''


def unifyModifyInp():
    global groupPm
    groupPm = pf.getOneGroupParamer()
    pm.repliceAll('S', 7, 'C', 11, groupPm)
    pm.saveFile()


'''
运行swmm产生一个[管网参数，观测点水位信息]的样本
'''


def getonesample():
    global groupPm
    unifyModifyInp()
    runModel()
    avgSW, maxSW, maxTSW = pm.getResult3('J11')
    maxTSW = maxTSW.split(':')
    # print(maxTSW)
    maxTNum = int(maxTSW[0]) * 60 + int(maxTSW[1])
    groupPm.append(avgSW)
    groupPm.append(maxSW)
    groupPm.append(maxTNum)
    return groupPm


'''
产生200个样本，存到文件
'''


def saveTxt(path):
    samples = []
    np.set_printoptions(suppress=True)
    for i in range(200):
        one = getonesample()
        samples.append(one)
    NpSamples = np.array(samples, 'float64')
    np.savetxt(path, NpSamples, fmt='%.5f', )


if __name__ == "__main__":
    # 'samples/samples.txt'
    path = args.argv[1]
    saveTxt(path)
