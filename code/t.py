import scipy.stats as stats 
import csv 

with open('verbal_memory_data.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    data = [row for row in csv_reader]

temp = []

plb = []
pla = []
pub = []
pua = []

for i in range(0, len(data)):
    for n in range(0, 6):
        pla.append(int(data[i][23 + n]))
        plb.append(int(data[i][17 + n]))

for i in range(0, len(data)):
    for n in range(0, 6):
        pua.append(int(data[i][39 + n]))
        pub.append(int(data[i][33 + n]))

# visual + verbal pxa, pxb | reaction time pxb, pxa
t_stat, p_val = stats.ttest_rel(pua, pub)

if t_stat > 0:
    one_tailed_p = p_val / 2
else:
    one_tailed_p = 1 - (p_val / 2)

print("T-statistic:", t_stat)
print("One-tailed p-value:", one_tailed_p)


