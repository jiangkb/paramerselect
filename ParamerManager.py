#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import re
import numpy as np

inpfile = ''
rptfile = ''


def repliceManning(gqName, inletNode, outletNode, Manning):
    global inpfile
    content = ''
    for line in inpfile.splitlines():
        newline = line
        if (line.find(gqName) >= 0 and line.find(inletNode) >= 0 and line.find(outletNode) > 0):
            str = line.split()
            newline = re.sub(str[4], Manning, newline)
        content = content + newline + '\n'
    inpfile = content


def findManning(gqName, inletNode, outletNode):
    global inpfile
    for line in inpfile.splitlines():
        if (line.find(gqName) >= 0 and line.find(inletNode) >= 0 and line.find(outletNode) > 0):
            str = line.split()
            return str[4]


def repliceSubArea(tableName, nextTableName, areaName, index, value):
    global inpfile
    content = ''
    start, end = getTableByName(inpfile, tableName, nextTableName)
    current = 0
    for line in inpfile.splitlines():
        newline = line
        if (current > start and current < end):
            if (line.find(areaName) >= 0):
                str = line.split()
                newline = re.sub(str[index], value, newline)
        content = content + newline + '\n'
        current += 1
    inpfile = content


def getSubArea(tableName, nextTableName, areaName, index):
    global inpfile
    start, end = getTableByName(inpfile, tableName, nextTableName)
    current = 0
    for line in inpfile.splitlines():
        if (current > start and current < end):
            if (line.find(areaName) >= 0):
                str = line.split()
                return str[index]


def readResult(filestr, tableName, nextTableName, nodeName, nodeType):
    start, end = getTableByName(filestr, tableName, nextTableName)
    current = 0
    for line in filestr.splitlines():
        if (current > start and current < end):
            if (line.find(nodeName) >= 0 and line.find(nodeType) >= 0):
                str = line.split()
                avg = float(str[2])
                max = float(str[3])
                return avg, max
        current += 1
    return float(-1),float(-1),'00:-1'


def getTableByName(filestr, tableName, nextTableName):
    start, end = 0, 0
    current = 0
    for line in filestr.splitlines():
        if (line.find(tableName) >= 0):
            start = current
        if (line.find(nextTableName) >= 0):
            end = current
        current += 1
    return start, end


def changeManning(value):
    repliceManning('gq1', 'j1', 'j2', str(value))


def getManning():
    return findManning('gq1', 'j1', 'j2')


def changeNimperv(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 1, str(value))


def changeNperv(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 2, str(value))


def changeSimperv(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 3, str(value))


def changeSperv(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 4, str(value))


def changeCZero(value):
    repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 5, str(value))


def getResult(path='D:\SWMMH\Examples\\test2.rpt'):
    rpt = open(path, 'r')
    con = ''
    for line in rpt:
        con += line
    return readResult(con, 'Node Depth Summary', 'Node Inflow Summary', 'pfk1', 'OUTFALL')


def readInpFile(path='example2\\Example.inp'):
    global inpfile
    inpfile = ''
    inp = open(path, 'r')
    for line in inp:
        inpfile += line


def readRptFile(path='example2\\Example.rpt'):
    global rptfile
    rptfile = ''
    rpt = open(path, 'r')
    for line in rpt:
        rptfile += line


def getCurrentInp():
    global inpfile
    return inpfile


def setinpfile(inpstr):
    global inpfile
    inpfile = inpstr
    saveFile()


def saveFile(path='example2\\Example.inp'):
    global inpfile
    newinp = open(path, 'w')
    newinp.write(inpfile)
    newinp.close()


# 使用全局变量内部声明
def runInp():
    global inpfile
    inp = open('D:\SWMMH\Examples\\test.inp', 'r')
    for line in inp:
        inpfile += line

    # repliceManning('gq1', 'j1', 'j2', '0.03')
    # repliceSubArea('SUBAREAS', 'INFILTRATION', 'zmj1', 1, '0.04')
    changeCZero(23)
    newinp = open('example2\\Example.inp', 'w')
    newinp.write(inpfile)
    newinp.close()
    inp.close()
    print(inpfile)


def runRpt():
    rpt = open('D:\SWMMH\Examples\\test.rpt', 'r')
    con = ''
    for line in rpt:
        con += line
    avg, max = readResult(con, 'Node Depth Summary', 'Node Inflow Summary', 'pfk1', 'OUTFALL')
    rpt.close()
    print(avg, max)


def repliceSubArea5(areaName, value):
    global inpfile
    content = ''
    start, end = getTableByName(inpfile, 'SUBAREAS', 'INFILTRATION')
    current = 0
    for line in inpfile.splitlines():
        newline = line
        if (current > start and current < end):
            if (line.find(areaName) >= 0):
                strP = line.split()
                for i in range(5):
                    newline = newline.replace(strP[i + 1], str(value[i]), 1)
                    # newline = re.sub(strP[i + 1], str(value[i]), newline)
        content = content + newline + '\n'
        current += 1
    inpfile = content


def repliceSubArea3(areaName, value):
    global inpfile
    content = ''
    start, end = getTableByName(inpfile, 'INFILTRATION', 'JUNCTIONS')
    current = 0
    for line in inpfile.splitlines():
        newline = line
        if (current > start and current < end):
            if (line.find(areaName) >= 0):
                # print('before-------->',newline)
                strP = line.split()
                for i in range(3):
                    newline = newline.replace(strP[i + 1], str(value[i]), 1)
                    # newline = re.sub(strP[i + 1], str(value[i]), newline)
                    # print('after--------->', newline)
        content = content + newline + '\n'
        current += 1
    inpfile = content


def changeSubArea8(areaName, value):
    repliceSubArea5(areaName, value[:5])
    repliceSubArea3(areaName, value[5:])


def repliceAreas(reg, value):
    for i in range(len(value)):
        areaName = reg + str(i + 1)
        changeSubArea8(areaName, value[i])


def repliceMannin(pipName, value):
    global inpfile
    content = ''
    start, end = getTableByName(inpfile, 'CONDUITS', 'XSECTIONS')
    current = 0
    for line in inpfile.splitlines():
        newline = line
        if (current > start and current < end):
            strP = line.split()
            if (len(strP) > 0 and strP[0][:1] == pipName):
                index = int(strP[0][1:])
                # print(pipName + str(index),strP[4],str(value[index-1]))
                newline = newline.replace(strP[4], str(value[index - 1]), 1)
                # newline = re.sub(strP[4], str(value[index-1]), newline)
        content = content + newline + '\n'
        current += 1
    inpfile = content


def repliceGeom(pipName, value):
    global inpfile
    content = ''
    start, end = getTableByName(inpfile, 'XSECTIONS', 'TIMESERIES')
    current = 0
    for line in inpfile.splitlines():
        newline = line
        if (current > start and current < end):
            strP = line.split()
            if (len(strP) > 0 and strP[0][:1] == pipName):
                index = int(strP[0][1:])
                # print(newline.index('1.0'),len(newline))
                # print('before---------', strP[2], strP[3])
                # newline = newline.replace(strP[2], str(value[index - 1][0]), 1)
                newline = newline.replace(strP[3], str(value[index - 1]), 1)
                # newline = re.sub(strP[2], str(value[index-1][0]), newline)
                # newline = re.sub(strP[3], str(value[index - 1][1]), newline)
                strP = newline.split()
                # print('after---------', strP[2], strP[3])
                # index += 1
        content = content + newline + '\n'
        current += 1
    inpfile = content


def getMaxGeom(pipName, lens):
    maxArr = range(lens)
    global inpfile
    start, end = getTableByName(inpfile, 'XSECTIONS', 'TIMESERIES')
    current = 0
    for line in inpfile.splitlines():
        if (current > start and current < end):
            strP = line.split()
            if (len(strP) > 0 and strP[0][:1] == pipName):
                index = int(strP[0][1:])
                maxArr[index] = float(strP[2])
        current += 1
    return maxArr


def repliceAll(areaRex, areaNum, pipRex, pipNum, value):
    # 替换所有area参数
    for i in range(areaNum):
        areaName = areaRex + str(i + 1)
        changeSubArea8(areaName, value[:8])
    # 替换管道参数
    manning = value[8]
    geom = value[9]
    manningArr = []
    geomArr = []
    for i in range(pipNum):
        manningArr.append(manning)
        geomArr.append(geom)
    repliceMannin(pipRex, manningArr)
    repliceGeom(pipRex, geomArr)


def getResult3(nodeName):
    readRptFile()
    global rptfile
    start, end = getTableByName(rptfile, 'Node Depth Summary', 'Node Inflow Summary')
    current = 0
    for line in rptfile.splitlines():
        if (current > start and current < end):
            if (line.find(nodeName) >= 0):
                str = line.split()
                avg = float(str[2])
                max = float(str[3])
                maxTime = str[6]
                return avg, max, maxTime
        current += 1
    return 'no value', 'no value'


# 0.011-0.024
# manningRange = np.linspace(0.011, 0.024, 10, True)
# print(manningRange)

# N-imperv 0.005-0.05
# N_impervRange=np.linspace(0.005,0.05, 10, True)
# print(N_impervRange)
readInpFile()
if __name__ == "__main__":
    readInpFile()
    value = range(8)
    repliceMannin('C', range(11))
    c = []
    for i in range(11):
        if (len(c) <= 0):
            c = np.linspace(1, 2, 2)
        a = np.linspace(1, 2, 2)
        c = np.row_stack((c, a))
    repliceGeom('C', c)

    changeSubArea8('S1', value)
    saveFile()
    getResult3('J1')
