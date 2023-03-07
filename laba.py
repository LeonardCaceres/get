import numpy as np
import matplotlib.pyplot as plt
import csv

x2 = []
y2 = []
with open('laba2.csv') as f:
    reader = csv.reader(f)
    flag = 0
    for row in reader:
        x1 = row[0]
        y1 = row[1]
        x1 = int(x1[:2]) * 3600 + int(x1[5:7]) * 60 + int(x1[10:12]) - 9 * 3600 - 37 * 60 - 31
        y1 = float(y1) + 273.15
        if (x1 >= 0 and x1 <= 9077):
            if x1 == 172:
                flag += 1
            if flag == 2:
                break
            if x1 != 6299:
                x2.append(x1)
                y2.append(y1)
for i in range(len(x2)):
    print(x2[i], " , ", y2[i])
fig, ax = plt.subplots()
for i in range(0,len(x2)):
    ax.plot(x2[i], y2[i], color='red', marker='.')
ax.set_ylabel('T(комнатная температура в кельвинах), К')
ax.set_xlabel('t(время), с')
ax.set_yticks(np.arange(290,311,0.1))
ax.set_xticks(np.arange(0,9100,400))
ax.grid(color='black', linewidth=0.3)
ax.legend(loc='lower right')
plt.ylim([290,292])
plt.xlim([0,9300])
plt.show()