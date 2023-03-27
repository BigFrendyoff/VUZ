import datetime
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

# # task, variant, group, time, status, achievements
statuses = pd.read_csv("statuses.csv")

groups = [i for i in statuses['group']]
status = [i for i in statuses['status']]

res = dict()

for i in range(len(status)):
    if groups[i] not in res.keys() and (status[i] == 2 or status[i] == 5):
        res[groups[i]] = 1
    elif status[i] == 2 or status[i] == 5:
        res[groups[i]] += 1
mx = max(res.values())
for i in res.keys():
    if res[i] == mx:
        print(i)