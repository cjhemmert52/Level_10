import pandas as pd

data = pd.read_csv("cfb.csv")

while True:
    try:
        season = int(input('Enter a season to analyze: '))
    except ValueError:
        print('Enter a valid season from 2013 to 2020')
        continue

    season_data = data[data['Season'] == season]

    if season_data.empty:
        print('No data was found, try again')
    else:
        print(season_data)
        break

#Add list of teams to a list with other teams with similar win quantities
categories = {
    '10 or more wins': [],
    '8-9 wins': [],
    '6-7 wins': [],
    'Fewer than 6 wins': []
}

for index, row in season_data.iterrows():
    team = row['Team']
    wins = row['Win']

    if pd.isna(wins):
        continue

    if wins >= 10:
        categories['10 or more wins'].append(team)
    elif wins >= 8:
        categories['8-9 wins'].append(team)
    elif wins >= 6:
        categories['6-7 wins'].append(team)
    else:
        categories['Fewer than 6 wins'].append(team)

print(f'College Football Results for {season}')