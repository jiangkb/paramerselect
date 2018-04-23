#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from pyswmm import Simulation
import ParamerFactory as pf
import ParamerManager as pm

def modifyInp():
    print()

def modifysubArea():
    print()

def modifyPip():
    pip11=[]
    for i in range(11):
        pip11.append(pf.pipParamer(5))
    pm.repliceGeom('C',pip11)
    print(pip11,pm.getCurrentInp())

def runModel(path='example2\\Example.inp'):
    sim = Simulation(path)
    sim.execute()

def compareError():
    print()

if __name__ == "__main__":
    modifyPip()