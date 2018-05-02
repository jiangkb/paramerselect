import os
path='samples/'
ls = os.listdir(path)
count = 0
for i in ls:
    if os.path.isfile(os.path.join(path,i)):
        count += 1
print (count)
for i in range(count,count+10):
    print(i)


