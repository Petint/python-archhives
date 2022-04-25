import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def read_data():
    library = pd.read_csv("library.csv")
    print(library.head(5))
    print("--------------------------------------------------------------------------------------------------------------------")
    library.drop(["Former owner", "Contributors", "Corporate Author",
                  "Corporate Contributors", "Edition Statement"],
                 axis= 1, inplace= True)
    print(library.head(5))
    print("-----------------------------------------------------------------------------------------------------------------------------")
    library.drop(columns=["Shelfmarks"], inplace= True)
    print(library.head(5))
# read_data()

def indexing_data():
    library = pd.read_csv("library.csv")
    print(library["Date of Publication"].is_unique)
    library.set_index("Date of Publication")
    print(library.head(100))

# indexing_data()


def row_data(index):
    library = pd.read_csv("library.csv")
    library = library.set_index("Identifier")
    print(library.loc[index])

# row_data(1808)

def row_data2(row):
    library = pd.read_csv("library.csv")
    library = library.set_index("Identifier")
    print(library.iloc[row])

# row_data2(0)

def clean_data():
    library = pd.read_csv("library.csv")
    library = library.set_index("Identifier")
    print(library.loc[1982:, "Date of Publication"].head(20))

    extr = library['Date of Publication'].str.extract(r'^(\d{4})',
                                                      expand= False)
    library['Date of Publication'] = pd.to_numeric(extr)
    print(library.loc[1982:, "Date of Publication"].head(20))


    print(library['Date of Publication'].isnull().sum() / len(library))
    avg = round(library['Date of Publication'].mean())
    library['Date of Publication'] = library['Date of Publication'].fillna(avg)
    print(library.loc[1982:, "Date of Publication"].head(20))
clean_data()

