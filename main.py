#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from pyswmm import Simulation
import ParamerFactory as pf
import ParamerManager as pm
import numpy as np

SubareaPm=[]
PipPm=[]
def modifyInp():
    global PipPm
    global SubareaPm
    PipPm=modifyPip()
    SubareaPm=modifysubArea()
    pm.saveFile()

def modifysubArea(areas=7):
    subareas=[]
    for i in range(areas):
        subareas.append(pf.subAreaParamer())
    pm.repliceAreas('S',subareas)
    return subareas

def modifyPip(pips=11):
    pip11 = []
    for i in range(pips):
        pip11.append(pf.pipParamer(1))
    pm.repliceGeom('C', pip11)
    return pip11

def runModel(path='example2\\Example.inp'):
    sim = Simulation(path)
    sim.execute()


def computeDelta(pointName,avg,mas):
    delta=0;
    avgSW,maxSW,maxTSW=pm.getResult3(pointName)
    delta=abs(avg-avgSW)+abs(mas-maxSW)
    return delta


if __name__ == "__main__":
    modifyInp()
    runModel()
    a=computeDelta('J6',0.07,0.25)
    print(a,SubareaPm,PipPm)