# tuknu pravym na projekt- open in - explorer - tím si uložím do projektu soubor

# import wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")

import pandas

jobs = pandas.read_csv("jobs.csv")

# print(jobs.columns)
# print(jobs.shape[0])
# print(jobs.iloc[9])
print(jobs.iloc[11:19, [5,7]])
