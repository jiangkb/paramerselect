#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from pyswmm import Simulation
import numpy as np
import ParamerFactory as pf
import ParamerManager as pm
import sys as args

PipPm = []
'''
修改管道淤积参数
'''


def modifyInp():
    global PipPm
    PipPm = modifyPip()
    pm.saveFile()


'''
获取管的最大高度并根据最大高度生成随机淤积，在替换inp,并返回当前管道淤积深度list
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
运行swmm产生一个[管网参数，观测点水位信息]的样本
'''


def getonesample():
    global PipPm
    modifyInp()
    runModel()
    avgSW, maxSW, maxTSW = pm.getResult3('J11')
    maxTSW = maxTSW.split(':')
    # print(maxTSW)
    maxTNum = int(maxTSW[0]) * 60 + int(maxTSW[1])
    PipPm.append(avgSW)
    PipPm.append(maxSW)
    PipPm.append(maxTNum)
    return PipPm


'''
产生200个样本，存到文件
'''


def saveTxt(path):
    samples = []
    np.set_printoptions(suppress=True)
    for i in range(200):
        one = getonesample()
        print(one)
        samples.append(one)
    NpSamples = np.array(samples, 'float64')
    # 决定是否要保存
    np.savetxt(path, NpSamples)


if __name__ == "__main__":
    # 'samples/samples.txt'
    path = args.argv[1]
    saveTxt(path)
