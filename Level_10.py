import pandas as pd

data = pd.read_csv("cfb.csv")

print(data)

def get_year(data):
    season = input('Enter a season to analyze: ')
    return season