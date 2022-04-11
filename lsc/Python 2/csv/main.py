import csv
import pandas as pd     # Pandaz & Gorillaz
import matplotlib.pyplot as plt

desired_width = 500
pd.set_option("display.width", desired_width)
pd.set_option("display.max_columns", 10)


def opencsv(filename: str):
    csvfile = open(filename, newline='')
    data = csv.reader(csvfile, delimiter=" ")
    for row in data:
        print(' '.join(row))


def openwithpandas(filename: str):
    csvfile = pd.read_csv(filename)
    print(csvfile.head(20))


def opencols(filename: str):
    csvfile = pd.read_csv(filename, usecols=["Age", "Name"])
    print(csvfile.head(10))
    sussum = csvfile["Age"].sum()
    row = len(csvfile["Age"])
    avg = sussum / row
    print(round(avg, 0))


def oldestwinner():
    csvfile = pd.read_csv("oscar_age_female.csv", usecols=["Age", "Name"])
    max_age = max(csvfile['Age'])
    myrow = csvfile[csvfile["Age"] == max_age]
    print(f"The oldes winer is {0} years old, and she is {1}", str(myrow.iloc[0, 0]), str(myrow.iloc[0, 1]))
    # print(myrow)


def fargowin():
    csvf = pd.read_csv("oscar_age_female.csv", usecols=["Year", "Movie"], skipinitialspace=True)
    mr = csvf[csvf["Movie" == "Fargo"]]
    print(str(mr.iloc[0, 1]) + " Oszkár díjat nyert " + str(mr.iloc[0, 0]) + "ban")


def datarow(row:int):
    csvf = pd.read_csv("oscar_age_female.csv")[row]
    miro = csvf.iloc
    print(miro)


def plotdata():
    csvf = pd.read_csv("oscar_age_female.csv")
    csvf.plot(x="Year", y="Age", kind='scatter')
    plt.title("Year - Age graph")
    plt.show()
# GnomeChomsky
# openCSV("oscar_age_female.csv")
# openWithPandas("oscar_age_female.csv")
# opencols("oscar_age_female.csv")
# oldestwinner()
# fargowin()
# datarow(1)
plotdata()
