import datetime
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


# task, variant, group, time, status, achievements
statuses = pd.read_csv("statuses.csv")

res = {}


groups = [i for i in statuses['group']]
variants = [i for i in statuses['variant']]
achievements = [len(eval(i)) for i in statuses['achievements']]

for i in range(len(groups)):
    if groups[i] not in res.keys():
        res[groups[i]] = {variants[i]:achievements[i]}
    else:
        if variants[i] not in res[groups[i]]:
            res[groups[i]][variants[i]] = achievements[i]
        else:
            res[groups[i]][variants[i]] += achievements[i]
print(res)
srt = []
for i in res.keys():
    srt.extend([j for j in sorted(res[i].values())])

srt = sorted(srt, reverse=True)[:10]
print(srt)

ans = []
for i in res.items():
    for j in i[1].items():
       if j[1] in srt:
           ans.append((i[0], j[0]))
print(ans)