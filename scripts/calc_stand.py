
import numpy as np

arr = []
fp = './distribution_top500versions.csv'
with open(fp, 'r') as f:
    for line in f:
        val, freq = line.split(',')
        for i in range(int(freq)):
            arr.append(int(val))

# print(arr)
Arr = np.array(arr)

print("Standard Deviation : ", np.std(Arr))
print("Min : ", np.min(Arr))
print("Max : ", np.max(Arr))
print("Mean : ", np.mean(Arr))
print("Mediam : ", np.median(Arr))