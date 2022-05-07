import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option("display.max_rows", None)
csvFile = pd.read_csv("deniro.csv", skipinitialspace=True)  # , index_col="Year")
print(csvFile)


# colnames
col_names = list(csvFile.columns)
print(col_names)

max_score = min(csvFile['Score'])
print(csvFile[csvFile['Score'] == max_score])
