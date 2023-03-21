import datetime
import pandas as pd
import sklearn
from matplotlib import pyplot as plt
import seaborn as sb


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


# id, task, variant, group, time

messages = pd.read_csv("messages.csv")

res = [{} for i in range(8)]

tasks = [i for i in messages['task']]
dates = [f'{parse_time(i).month}.{parse_time(i).day}' for i in messages['time']]
for i in range(len(tasks)):
    if dates[i] not in res[tasks[i]].keys():
        res[tasks[i]][dates[i]] = 1
    else:
        res[tasks[i]][dates[i]] += 1
plt.figure(figsize=(15, 10))
for i in range(len(res)):
    plt.plot(res[i].keys(), res[i].values(), label=f"Задание {i + 1}")
plt.legend()

plt.show()
