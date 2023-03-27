import datetime
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

plt.figure(figsize=(60,10))
# id, task, variant, group, time
messages = pd.read_csv("messages.csv")

groups = [i for i in messages['group']]
sb.countplot(x=groups)
plt.show()