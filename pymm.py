#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from pyswmm import Simulation

sim = Simulation('example2\\Example.inp')
#sim.report()
sim.execute()
sim.close()

