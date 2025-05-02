# Get batting stats for the 2023 season

from pybaseball import batting_stats

stats = batting_stats(2023)
print(stats.head())

# Print all column names
for col in stats.columns:
    print(col)



# Get Real Time Game Status

import requests
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")
url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={today}&expand=schedule.linescore"

res = requests.get(url)
data = res.json()

for date in data['dates']:
    for game in date['games']:
        teams = game['teams']
        away_team = teams['away']['team']['name']
        home_team = teams['home']['team']['name']
        away_score = teams['away'].get('score', 0)
        home_score = teams['home'].get('score', 0)
        status = game['status']['detailedState']
        
        print(f"{away_team} ({away_score}) at {home_team} ({home_score}) - Status: {status}")


from pybaseball import batting_stats
import pandas as pd
from datetime import datetime

# Get the current year
year = datetime.now().year

# Pull season batting stats
df = batting_stats(year)

# Select key sabermetric columns
columns_of_interest = ['Name', 'Team', 'PA', 'HR', 'BB%', 'K%', 'wRC+', 'wOBA', 'ISO', 'WAR']
df_subset = df[columns_of_interest]

# Filter to players with 50+ plate appearances
df_filtered = df_subset[df_subset['PA'] >= 50]

# Sort by wRC+ descending
df_sorted = df_filtered.sort_values(by='WAR', ascending=False)

# Show top 10 hitters by wRC+
print(df_sorted.head(10))

from pybaseball import statcast_batter, playerid_lookup
from datetime import datetime, timedelta

print("\nStatcast Data for Juan Soto (Last 14 Days):")
first_name = "Juan"
last_name = "Soto"

# Lookup player ID
player_info = playerid_lookup(last_name, first_name)

if player_info.empty:
    print("Error: Player not found.")
else:
    player_id = player_info.iloc[0]["key_mlbam"]

    # Get data from past 14 days
    today = datetime.today().date()
    start_date = today - timedelta(days=14)

    df_statcast = statcast_batter(start_date.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d"), player_id)

    if df_statcast.empty:
        print("No statcast data found for the last 14 days.")
    else:
        print(df_statcast.head())

    print(df_statcast.columns)
    print(df_statcast.head())