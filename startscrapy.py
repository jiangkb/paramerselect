import os


# 计算文件个数
path='samples/'
ls = os.listdir(path)
count = 0
for i in ls:
    if os.path.isfile(os.path.join(path,i)):
        count += 1

#运行一次多了200*5个
for i in  range(count,count+1):
    print('start---------->')
    order='python main.py samples/samples'+str(i)
    print('end------------>',order)
    os.system(order)