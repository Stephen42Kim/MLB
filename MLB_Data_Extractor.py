# Import packages

from pybaseball import (
    batting_stats,
    statcast,
    statcast_batter,
    statcast_pitcher,
    playerid_lookup,
    pitching_stats,
    batting_stats
)
import pandas as pd
from datetime import datetime, timedelta
import requests

import warnings
warnings.filterwarnings("ignore", category=FutureWarning, message=".*errors='ignore'.*")


# ---------------------------------------
# 1. Get Season Batting Stats (2023)
# ---------------------------------------
stats = batting_stats(2023)
print(stats.head())

# Optional: print column names
print("Batting Stats Columns:")
print(stats.columns.tolist())

# ---------------------------------------
# 2. Real-Time Game Status
# ---------------------------------------
today = datetime.now().strftime("%Y-%m-%d")
url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={today}&expand=schedule.linescore"
res = requests.get(url)
data = res.json()

print(f"\nMLB Games on {today}:")
for date in data['dates']:
    for game in date['games']:
        teams = game['teams']
        away = teams['away']
        home = teams['home']
        print(f"{away['team']['name']} ({away.get('score', 0)}) at {home['team']['name']} ({home.get('score', 0)}) - Status: {game['status']['detailedState']}")

# ---------------------------------------
# 3. Filter & Sort Hitters by WAR
# ---------------------------------------
year = datetime.now().year
df = batting_stats(year)
columns_of_interest = ['Name', 'Team', 'PA', 'HR', 'BB%', 'K%', 'wRC+', 'wOBA', 'ISO', 'WAR']
df_filtered = df[df['PA'] >= 50][columns_of_interest]
df_sorted = df_filtered.sort_values(by='WAR', ascending=False)
print("\nTop 10 Hitters by WAR:")
print(df_sorted.head(10))

# ---------------------------------------
# 4. Statcast for Juan Soto (Last 14 Days)
# ---------------------------------------
print("\nStatcast Data for Juan Soto (Last 14 Days):")
soto_info = playerid_lookup('soto', 'juan')
if soto_info.empty:
    print("Error: Player not found.")
else:
    soto_id = soto_info.iloc[0]["key_mlbam"]
    today = datetime.today().date()
    start_date = today - timedelta(days=14)
    soto_data = statcast_batter(start_date.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d"), soto_id)
    soto_data.to_excel("C:\\Users\\Stephen\\Desktop\\SolariValinor\\MLB\\soto_statcast_batter.xlsx", index=False)

    if soto_data.empty:
        print("No statcast data found for the last 14 days.")
    else:
        print(soto_data.head())

# ---------------------------------------
# 5. Statcast: David Ortiz Batting
# ---------------------------------------   
print("\nDavid Ortiz Statcast Data:")
ortiz_info = playerid_lookup('ortiz', 'david')
if not ortiz_info.empty:
    ortiz_id = ortiz_info.iloc[0]['key_mlbam']
    
    # Filter all events where he was the batter
    data_all = statcast('2016-04-01', '2016-06-01')  # Ortiz's final season
    data_batter = data_all[data_all['batter'] == ortiz_id]
    print("Ortiz Batting Events Columns:", data_batter.columns.tolist())

    # Historical batter stats
    ortiz_stats = statcast_batter('2008-04-01', '2017-07-15', ortiz_id)
    print("Ortiz Batting Stats Columns:", ortiz_stats.columns.tolist())
else:
    print("David Ortiz not found.")

# ---------------------------------------
# 6. Statcast: Justin Verlander Pitching
# ---------------------------------------
print("\nJustin Verlander Statcast Data:")
verlander_info = playerid_lookup('verlander', 'justin')
if not verlander_info.empty:
    verlander_id = verlander_info.iloc[0]['key_mlbam']

    data_all_pitching = statcast('2024-04-01', '2024-05-01')  # Update range as needed
    data_pitcher = data_all_pitching[data_all_pitching['pitcher'] == verlander_id]
    print("Verlander Pitching Events Columns:", data_pitcher.columns.tolist())

    data_pitcher.to_excel("C:\\Users\\Stephen\\Desktop\\SolariValinor\\MLB\\pitcher_stats.xlsx", index=False)

    # Historical pitching stats
    verlander_stats = statcast_pitcher('2008-04-01', '2019-07-15', verlander_id)
    print("Verlander Pitching Stats Columns:", verlander_stats.columns.tolist())

    data_pitcher.to_excel("C:\\Users\\Stephen\\Desktop\\SolariValinor\\MLB\\verlander_statcast_pitcher.xlsx", index=False)
else:
    print("Justin Verlander not found.")


print(data_pitcher)
print(verlander_stats)

