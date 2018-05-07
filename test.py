import os
import numpy as np

path = 'samples/'
ls = os.listdir(path)
count = 0
for i in ls:
    if os.path.isfile(os.path.join(path, i)):
        fileName = 'samples' + str(count)
        if (count == 0):
            samples = np.loadtxt(path + fileName)
        else:
            temp = np.loadtxt(path + fileName)
            samples = np.concatenate((samples, temp))
        count += 1

for a in samples:
    print(a)
print(len(samples), samples.shape)
