# paramerselect
利用swmm模型生成训练样本
# 1.项目文件简介
## ParamerFactory.py
主要用于生成各种各样的参数
## ParamerManager.py
用于修改.INP和读取.RPT文件
## main.py
用于装配参数，并运行swmm模型，生成样本
## startscrapy.py   ----->  项目启动入口  
用于控制main启动  运行 python startscrapy.py  项目启动
## test.py
测试脚本
## samlpe文件夹
sample0-N 一个样本文件含有200个样本

# 运行环境
1. python 3.6  32位
2. pyswmm模块   请用pip install pyswmm 安装
