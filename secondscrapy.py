import os


# 计算文件个数
path='secondSamples/'
ls = os.listdir(path)
count = 0
for i in ls:
    if os.path.isfile(os.path.join(path,i)):
        count += 1

#运行一次多了200*5个
for i in  range(count,count+5):
    print('start---------->')
    order='python secondadjust.py secondSamples/samples'+str(i)
    print('end------------>',order)
    os.system(order)