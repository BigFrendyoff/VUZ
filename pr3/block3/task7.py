import datetime
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


# # task, variant, group, time, status, achievements
statuses = pd.read_csv("statuses.csv")

tasks = [i + 1 for i in statuses['task']]
status = [i for i in statuses['status']]

chked = dict()
failed = dict()

for i in range(len(status)):
    if tasks[i] not in chked.keys() and (status[i] == 2 or status[i] == 5):
        chked[tasks[i]] = 1
    elif tasks[i] not in failed.keys() and (status[i] == 3 or status[i] == 6):
        failed[tasks[i]] = 1
    elif status[i] == 2 or status[i] == 5:
        chked[tasks[i]] += 1
    elif status[i] == 3 or status[i] == 6:
        failed[tasks[i]] += 1

chk_vals = list(chked.values())
fld_vals = list(failed.values())

relation = [fld_vals[i] / chk_vals[i] for i in range(len(chk_vals))]
print(relation)
print(max(relation))
fig, ax = plt.subplots()

ax.bar(chked.keys(), chked.values(), width=0.7)
ax.bar(failed.keys(), failed.values(), width=0.5)
plt.show()
