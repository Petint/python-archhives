import pandas as pd
from matplotlib import pyplot as plt

pd.set_option("display.max_rows", None)
csvFile = pd.read_csv("deniro.csv", skipinitialspace=True, usecols=["Score", "Year"])  # , index_col="Year"),
csvFile.plot(x="Year", y="Score", kind="scatter")
plt.title("Year - Score")
plt.show()
