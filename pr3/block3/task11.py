import datetime
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


games = pd.read_csv("GAMES.csv", sep=';')

plt.figure(figsize=(30, 10))
sb.countplot(x=games['year'])
plt.show()