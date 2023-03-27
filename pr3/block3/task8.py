import datetime
import logging

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


# # task, variant, group, time, status, achievements
statuses = pd.read_csv("statuses.csv")

groups = [i for i in statuses['group']]
achievements = [len(eval(i)) for i in statuses['achievements']]

res = dict()

plt.figure(figsize=(70, 10))

for i in range(len(groups)):
    if groups[i] not in res.keys():
        res[groups[i]] = achievements[i]
    else:
        res[groups[i]] += achievements[i]

plt.bar(res.keys(), res.values())
plt.show()
