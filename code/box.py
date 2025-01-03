import matplotlib.pyplot as plt
import csv

with open('visual_memory_data.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    data = [row for row in csv_reader]

temp = []

plb = []
pla = []
pub = []
pua = []

for i in range(0, len(data)):
    if i == 30:
        pass
    else:
        for n in range(0, 6):
            pla.append(int(data[i][23 + n]))
            plb.append(int(data[i][17 + n]))
            pua.append(int(data[i][39 + n]))
            pub.append(int(data[i][33 + n]))


temp = [plb, pla, pub, pua]

fig = plt.figure(figsize=(7, 7))
ax = plt.axes()
positions = [1, 1.25, 1.5, 1.75]

box = plt.boxplot(temp, patch_artist=True, positions=positions)

for patch in box['boxes']:
    patch.set_facecolor('white')

ax.set_facecolor('#E5ECF6')
plt.xlabel("Game Type", fontsize = 15)
plt.grid(True, axis='y', linestyle='--', mfc = '#111111')
plt.xticks([1, 1.25, 1.5, 1.75], ['Platformer \nBefore', 'Platfromers \nAfter', 'Puzzle \nBefore', 'Puzzle \nAfter' ])
plt.ylabel("Verbal Memory (words)", fontsize = 15)
plt.xticks(fontsize = 15) 
plt.yticks(fontsize = 15) 
#plt.title("Reaction Time Spread in Platformer and Puzzle games")
plt.show()
