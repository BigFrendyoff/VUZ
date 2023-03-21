import datetime
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


# id, task, variant, group, time
messages = pd.read_csv("messages.csv")

tasks = [i + 1 for i in messages["task"]]

sb.countplot(x=tasks)
plt.show()
