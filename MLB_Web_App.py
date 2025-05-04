
# STATCAST PITCHER
from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup

# find Chris Sale's player id (mlbam_key)
playerid_lookup('sale','chris')

# statcast_pitcher(start_dt=[yesterday's date], end_dt=None, player_id)
# get all available data
data = statcast_pitcher('2017-07-01', '2017-07-15', player_id=519242)
print(data)

# get data for July 15th, 2017
data = statcast_pitcher('2017-07-15', '2017-07-15', player_id=519242)
print(data)

# STATCAST PITCHER VELO BARRELS
from pybaseball import statcast_pitcher_exitvelo_barrels

# statcast_pitcher_exitvelo_barrels(year, minBBE=[qualified])
# minBBE: The minimum number of batted ball against events for each pitcher. 
# If a player falls below this threshold, they will be excluded from the results. 
# If no value is specified, only qualified pitchers will be returned.
# get data for all qualified pitchers in 2019
data = statcast_pitcher_exitvelo_barrels(2019)
print(data)

# get data for pitchers with a minimum of 100 batted ball events in 2019
data = statcast_pitcher_exitvelo_barrels(2019, 100)
print(data)

# STATCAST PITCHER EXPECTED STATS
from pybaseball import statcast_pitcher_expected_stats

# statcast_pitcher_expected_stats(year, minPA=[qualified])
# minPA: The minimum number of plate appearances against for each player. 
# If a player falls below this threshold, they will be excluded from the results. 
# If no value is specified, only qualified pitchers will be returned.
# get data for all qualified pitchers in 2019
data = statcast_pitcher_expected_stats(2019)
print(data)

# get data for pitchers with a minimum of 150 plate appearances against in 2019
data = statcast_pitcher_expected_stats(2019, 150)
print(data)

# STATCAST PITCHER PITCH ARSENAL
from pybaseball import statcast_pitcher_pitch_arsenal

# statcast_pitcher_pitch_arsenal(2019, minP=[qualified], arsenal_type="average_speed")
# arsenal_type: The type of stat to retrieve for the pitchers' arsenals. Options include 
# ["average_speed", "n_", "average_spin"], where "n_" corresponds to the percentage share 
# for each pitch. If no value is specified, it will default to average speed.
# get average pitch speed data for all qualified pitchers in 2019
data = statcast_pitcher_pitch_arsenal(2019)
print(data)

# get average pitch spin data for pitchers with at least 200 pitches in 2019
data = statcast_pitcher_pitch_arsenal(2019, minP=200, arsenal_type="average_spin")
print(data)

# get percentage shares data for qualified pitchers in 2019
data = statcast_pitcher_pitch_arsenal(2019, arsenal_type="n_")
print(data)

# STATCAST PITCHER PITCH ARSENAL STATS
from pybaseball import statcast_pitcher_arsenal_stats

# get data for all pitchers with 25 or more plate appearances against in 2019
data = statcast_pitcher_arsenal_stats(2019)
print(data)

# get data for all pitchers with 100 or more plate appearances against in 2019
data = statcast_pitcher_arsenal_stats(2019, minPA=100)
print(data)

# SEASON-LEVEL PITCHING DATA FROM FANGRAPHS
from pybaseball import pitching_stats

# pitching_stats(start_season, end_season=None, league='all', qual=1, ind=1)
# league: String. Either "all" for all data, "nl" for National League, "al" for 
# the American League, or "mnl" for all Negro League data. Defaults to "all", for 
# returning data on all teams. See FangraphsLeague definition for all leagues.
# qual: Integer. Minimum number of plate appearances to be included in the results. 
# Defaults to None, which is equivalent to the current Fangraphs "Qualified" PA 
# threshold from their leaderboard.
# ind: 1 or 0. Equals 1 if you want data returned at the individual season level. 
# Equals 0 if you want aggregate data over the seasons included in the query. With 
# ind=1 and a query spanning the 2010 through 2015 seasons, for example, you will get 
# each player's stats for 2010, 2011, 2012, 2013, 2014, and 2015 in a separate 
# observation. With ind=0, this same query returns one row per player with their 
# statistics aggregated over this period (either summed or averaged depending on 
# what's appropriate).
# get all of this season's pitching data so far
data = pitching_stats(2017)

# retrieve data on only players who have pitched 50+ innings this year
data = pitching_stats(2017, qual=50)
print(data)

# retrieve one row per player per season since 2000 (i.e.: who had the single most dominant season over this period?)
data = pitching_stats(2010, 2016)
print(data)

# retrieve aggregate player statistics from 2000 to 2016 (i.e.: who has the most wins over this period?)
data = pitching_stats(2010, 2016, ind=0)
print(data)





