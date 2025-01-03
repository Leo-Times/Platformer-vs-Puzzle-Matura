import matplotlib.pyplot as plt
import csv
import numpy as np

with open('verbal_memory_data.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    data = [row for row in csv_reader]

temp = []

x=[]
pl = []
pu = []
pl_a = 0
pu_a = 0

for i in range(0, len(data)):
    #print(i)
    if i == 30:
        pass
    else:
        x.append(data[i][0])
        pl.append((float(data[i][15+16])))
        pu.append((float(data[i][15+32])))
        pl_a += float(data[i][15+16])
        pu_a += float(data[i][15+32])

pl.append((pl_a/len(x)))
pu.append((pu_a/len(x)))

x.append('avg')

r = np.arange(len(pl))
r2 = r + 0.4

fig, ax = plt.subplots(dpi=100)
ax.bar(r, pl, color='#00c698', width=.4, label='Platformer')
ax.bar(r2, pu, color='#0045a5', width=.4, label='Puzzle')

ax.set_xticks(r + .2)
ax.set_xticklabels(x)

ax.set_xlabel("Participant", fontsize = 15)
ax.set_ylabel("Verbal Memory Delta (words)", fontsize = 15)
#ax.set_title("Reaction Time gains in Platformer games and Puzzle games")

ax.legend()

plt.xticks(fontsize = 15) 
plt.yticks(fontsize = 15) 

plt.legend(fontsize = 15)

plt.show()
