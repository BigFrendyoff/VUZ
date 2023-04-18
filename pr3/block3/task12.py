import datetime
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


games = pd.read_csv("GAMES.csv", sep=';')

years = [i for i in games["year"]]
genres = [i for i in games["genre"]]

res = {}

for i in range(len(years)):
    if years[i] != 'не издана':
        if (genres[i]) not in res.keys():
            res[genres[i]] = {years[i]: 1}
        else:
            if (years[i] not in res[genres[i]].keys()):
                res[genres[i]][years[i]] = 1
            else:
                res[genres[i]][years[i]] += 1
plt.figure(figsize=(40, 10))

for i in res.keys():
    plt.plot(res[i].keys(), res[i].values(), label=i)
plt.legend()
plt.show()