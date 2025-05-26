# Import packages

from pybaseball import get_splits, playerid_lookup
import pandas as pd
from datetime import datetime, timedelta
import requests

import warnings
warnings.filterwarnings("ignore", category=FutureWarning, message=".*errors='ignore'.*")


# Get the split stats and player info for batters
def batter_splits(batters):
    results = {}

    for player in batters:
        names = player.strip().split()
        first_name = " ".join(names[:-1])
        last_name = names[-1]

        # Get player ID using actual names
        lookup = playerid_lookup(last_name, first_name)
        if lookup.empty:
            print(f"Player {player} not found.")
            continue

        player_id = lookup.iloc[0]['key_bbref']

        # Get splits and player info
        try:
            splits, player_info = get_splits(player_id, player_info=True)
            results[player] = {
                "player_id": player_id,
                "splits": splits,
                "player_info": player_info
            }
        except Exception as e:
            print(f"Error retrieving data for {player} ({player_id}): {e}")
            continue

    return results

# Get the split stats and player info for pitchers
def pitcher_splits(pitchers):
    results = {}

    for player in pitchers:
        names = player.strip().split()
        first_name = " ".join(names[:-1])
        last_name = names[-1]

        # Get player ID using actual names
        lookup = playerid_lookup(last_name, first_name)
        if lookup.empty:
            print(f"Player {player} not found.")
            continue

        player_id = lookup.iloc[0]['key_bbref']

        # Get splits and player info
        try:
            splits = get_splits(player_id, pitching_splits=True)
            results[player] = {
                "player_id": player_id,
                "splits": splits,
                #"player_info": player_info
            }
        except Exception as e:
            print(f"Error retrieving data for {player} ({player_id}): {e}")
            continue

    return results



# ✅ Lists of players
batters = [
    'Adley Rutschman', 'Drake Baldwin', 'Dalton Rushing', 'Carson Kelly', 'Johah Heim',
    'Tyler Soderstrom', 'Cody Bellinger', 'Christian Encarnacion-Strand',
    'Brendan Donovan', 'Jordan Westburg', 'Matt McLain', 'Hye Seong Kim',
    'Jorge Polanco', 'Jake Burger', 'Zach McKinstry', 'Coby Mayo',
    'Jacob Wilson', 'Jeremy Pena', 'Willy Adames', 'Tommy Edman', 'Trevor Story',
    'Taylor Ward', 'Austin Hays', 'Colton Cowser', 'Chandler Simpson', 'Trent Grisham',
    'Victor Scott II', 'Seiya Suzuki', 'Shohei Ohtani'
]

pitchers = [
    'Paul Skenes', 'Pablo Lopez', 'Sonny Gray', 'Luis Castillo', 'Clay Holmes', 'Max Scherzer',
    'Ryan Pepiot', 'Jeffrey Springs', 'David Peterson', 'Tomoyuki Sugano', 'Chris Paddack',
    'Luis Guil', 'Logan Henderson', 'Shane Baz', 'Max Meyer', 'Zebby Matthews', 'Andrew Painter',
    'Shohei Ohtani', 'Tanner Scott', 'Pete Fairbanks', 'David Bednar', 'Dennis Santana',
    'Drew Pomeranz', 'Daniel Palencia'
]

batters1 = ['Adley Rutschman']
pitchers1 = ['Paul Skenes']

# ✅ Run
b_splits = batter_splits(batters1)
p_splits = pitcher_splits(pitchers1)

b_splits
p_splits

batting_df = b_splits['Adley Rutschman']['splits']

print(batting_df)
print(batting_df.index.names)

print(batting_df.index.get_level_values('Split'))

pitching_df = p_splits['Paul Skenes']['splits'][1]

print(pitching_df)
print(pitching_df.index.names)

print(pitching_df.index.get_level_values('Split'))


#for name, (df, info) in b_splits.items():
#    print(name)
#    print(df.head())

#for name, (df, info) in p_splits.items():
#    print(name)
#    print(df.head())

# Uncomment to save
# for name, df in bat_stats.items():
#     df.to_csv(f"{name.replace(' ', '_')}_batter.csv")

# for name, df in pitch_stats.items():
#     df.to_csv(f"{name.replace(' ', '_')}_pitcher.csv")


'''
from pybaseball import get_splits, playerid_lookup
name = "paul skenes"
name
names = name.strip().split()
names
first_name = " ".join(names[:-1])
first_name
last_name = names[-1]
last_name

data = playerid_lookup(last_name, first_name)
data
player_id = data.iloc[0]['key_bbref']
player_id
df = get_splits(player_id, pitching_splits=True)
df

data = playerid_lookup("skenes", "paul")
data
player_id = data.iloc[0]['key_bbref']
player_id
df, player_info_dict = get_splits(player_id, player_info=True)
df

g = 1
print(g)
'''