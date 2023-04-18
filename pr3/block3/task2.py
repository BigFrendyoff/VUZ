import datetime
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f').hour



# id, task, variant, group, time
messages = pd.read_csv("messages.csv")

# id, message_id, time, status
checks = pd.read_csv("checks.csv")

# task, variant, group, time, status, achievements
statuses = pd.read_csv("statuses.csv")

message_time = [parse_time(i) for i in messages['time']]

sb.countplot(x=message_time)
plt.show()