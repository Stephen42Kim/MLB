
# STATCAST PITCHER
from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup

# find Chris Sale's player id (mlbam_key)
playerid_lookup('sale','chris')

# statcast_pitcher(start_dt=[yesterday's date], end_dt=None, player_id)
# get all available data
data = statcast_pitcher('2017-07-01', '2017-07-15', player_id=519242)
print("STATCAST PITCHER")
print(data)

# get data for July 15th, 2017
data = statcast_pitcher('2017-07-15', '2017-07-15', player_id=519242)
print("STATCAST PITCHER 7/15")
print(data)
print(data.columns.tolist())

# STATCAST PITCHER EXIT VELO BARRELS
from pybaseball import statcast_pitcher_exitvelo_barrels

# statcast_pitcher_exitvelo_barrels(year, minBBE=[qualified])
# minBBE: The minimum number of batted ball against events for each pitcher. 
# If a player falls below this threshold, they will be excluded from the results. 
# If no value is specified, only qualified pitchers will be returned.
# get data for all qualified pitchers in 2019
data = statcast_pitcher_exitvelo_barrels(2019)
print("STATCAST PITCHER EXIT VELO BARRELS 2019")
print(data)

# get data for pitchers with a minimum of 100 batted ball events in 2019
data = statcast_pitcher_exitvelo_barrels(2019, 100)
print("STATCAST PITCHER EXIT VELO BARRELS 2019 MIN 100PA")
print(data)
print(data.columns.tolist())

# STATCAST PITCHER EXPECTED STATS
from pybaseball import statcast_pitcher_expected_stats

# statcast_pitcher_expected_stats(year, minPA=[qualified])
# minPA: The minimum number of plate appearances against for each player. 
# If a player falls below this threshold, they will be excluded from the results. 
# If no value is specified, only qualified pitchers will be returned.
# get data for all qualified pitchers in 2019
data = statcast_pitcher_expected_stats(2019)
print("STATCAST PITCHER EXPECTED STATS 2019")
print(data)

# get data for pitchers with a minimum of 150 plate appearances against in 2019
data = statcast_pitcher_expected_stats(2019, 150)
print("STATCAST PITCHER EXPECTED STATS 2019 MIN 150PA")
print(data)
print(data.columns.tolist())

# STATCAST PITCHER PITCH ARSENAL
from pybaseball import statcast_pitcher_pitch_arsenal

# statcast_pitcher_pitch_arsenal(2019, minP=[qualified], arsenal_type="average_speed")
# arsenal_type: The type of stat to retrieve for the pitchers' arsenals. Options include 
# ["average_speed", "n_", "average_spin"], where "n_" corresponds to the percentage share 
# for each pitch. If no value is specified, it will default to average speed.
# get average pitch speed data for all qualified pitchers in 2019
data = statcast_pitcher_pitch_arsenal(2019)
print("STATCAST PITCHER PITCH ARSENAL 2019")
print(data)

# get average pitch spin data for pitchers with at least 200 pitches in 2019
data = statcast_pitcher_pitch_arsenal(2019, minP=200, arsenal_type="avg_spin")
print("STATCAST PITCHER PITCH ARSENAL 2019 AVG PITCH SPIN MIN 200 PITCHES")
print(data)

# get percentage shares data for qualified pitchers in 2019
data = statcast_pitcher_pitch_arsenal(2019, arsenal_type="n_")
print("STATCAST PITCHER PITCH ARSENAL 2019 PERCENTAGE SHARES")
print(data)
print(data.columns.tolist())

# STATCAST PITCHER PITCH ARSENAL STATS
from pybaseball import statcast_pitcher_arsenal_stats

# get data for all pitchers with 25 or more plate appearances against in 2019
data = statcast_pitcher_arsenal_stats(2019)
print("STATCAST PITCHER PITCH ARSENAL STATS 2019")
print(data)

# get data for all pitchers with 100 or more plate appearances against in 2019
data = statcast_pitcher_arsenal_stats(2019, minPA=100)
print("STATCAST PITCHER PITCH ARSENAL STATS 2019 MIN 100PA")
print(data)
print(data.columns.tolist())

# STATCAST PITCHER PITCH MOVEMENT
# retrieves pitch movement stats for all qualified pitchers with a specified pitch type for a given year.
# statcast_pitcher_pitch_movement(2019, minP=[qualified], pitch_type="FF")
# pitch_type: The type of pitch to retrieve movement data on. Options include 
# ["FF", "SIFT", "CH", "CUKC", "FC", "SL", "FS", "ALL"]. Pitch names also allowed. 
# If no value is specified, it will default to "FF".
from python import statcast_pitcher_pitch_movement

# get data on qualified fastballs in 2019
data = statcast_pitcher_pitch_movement(2019)
print("STATCAST PITCHER QUALIFIED FASTBALL DATA 2019")
print(data)

# get data on pitchers who threw 30 or more changeups in 2019
data = statcast_pitcher_pitch_movement(2019, minP=30, pitch_type="CH")
print("STATCAST PITCHER WHO THREW 30 OR MORE CHANGEUPS IN 2019")
print(data)
print(data.columns.tolist())


# STATCAST PITCHER ACTIVE SPIN
# retrieves active spin stats on all of a pitchers' pitches in a given year.
# statcast_pitcher_active_spin(2019, minP=250)
from python import statcast_pitcher_active_spin

# get data on qualified pitchers in 2019
data = statcast_pitcher_active_spin(2019)
print("STATCAST PITCHER SPIN DATA 2019")
print(data)

# get data on pitchers who threw 100 or more pitches in 2019
data = statcast_pitcher_active_spin(2019, minP=100)
print("STATCAST PITCHER SPIN DATA 2019 MIN 100 PITCHES")
print(data)
print(data.columns.tolist())


# STATCAST PITCHER PERCENTILE RANKS
# retrieves percentile ranks for each player in a given year, 
# including batters with 2.1 PA per team game and 1.25 for pitchers. 
# It includes percentiles on expected stats, batted ball data, and spin rates, among others.
# statcast_pitcher_percentile_ranks(year)
from pybaseball import statcast_pitcher_percentile_ranks

# get data for all qualified pitchers in 2019
data = statcast_pitcher_percentile_ranks(2019)
print("STATCAST PITCHER PERCENTILE RANKS 2019")
print(data)
print(data.columns.tolist())

# STATCAST PITCHER SPIN DIRECTION COMPARISON
# pitch_a: The first pitch in the comparison. Valid pitches include "4-Seamer", "Sinker", 
# "Changeup", "Curveball", "Cutter", "Slider", and "Sinker". Defaults to "4-Seamer". Pitch codes also accepted.
# pitch_b: The second pitch in the comparison and must be different from pitch_a. Valid pitches 
# include "4-Seamer", "Sinker", "Changeup", "Curveball", "Cutter", "Slider", "Sinker". Defaults to 
# "Changeup". Pitch codes also accepted.
# minP: The minimum number of pitches of type pitch_a thrown. If a player falls below this threshold, 
# they will be excluded from the results. If no value is specified, only pitchers who threw 100
#  or more pitches will be returned.
# pitcher_pov: Boolean. If True, then direction of movement is from the pitcher's point of view. 
# If False, then it is from the batter's point of view.

# retrieves spin comparisons between two pitches for qualifying pitchers in a given year.
from pybaseball import statcast_pitcher_spin_dir_comp

# get data for fastball / changeup combos in 2020
data = statcast_pitcher_spin_dir_comp(2020)
print("STATCAST PITCHER FASTBALL/CHANGEUP COMBOS 2020")
print(data)

# get data for sinker / slider combos in 2020, with at least 50 sinkers thrown
data = statcast_pitcher_spin_dir_comp(2020, pitch_a="Sinker", pitch_b="Slider", minP=50)
print("STATCAST PITCHER SINKER/SLIDER COMBOS MIN 50 SINKERS 2020")
print(data)

# get data for sinker / slider combos in 2020 using pitch codes and from the batter's POV
data = statcast_pitcher_spin_dir_comp(2020, pitch_a="SIFT", pitch_b="SL", pitcher_pov=False)
print("STATCAST PITCHER SINKER/SLIDER COMBOS 2020 WITH PITCH CODES AND BATTER POV")
print(data)
print(data.columns.tolist())

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
print("SEASON-LEVEL PITCHING DATA FROM FANGRAPHS MIN 50IP")
print(data)

# retrieve one row per player per season since 2000 (i.e.: who had the single most dominant season over this period?)
data = pitching_stats(2010, 2016)
print("SEASON-LEVEL PITCHING DATA FROM FANGRAPHS SINGLE ROW PER PLAYER PER SEASON")
print(data)

# retrieve aggregate player statistics from 2000 to 2016 (i.e.: who has the most wins over this period?)
data = pitching_stats(2010, 2016, ind=0)
print("SEASON-LEVEL PITCHING DATA FROM FANGRAPHS AGGREGATE PLAYER STATS")
print(data)
print(data.columns.tolist())


# BATTING STATS
# returns season-level batting data from FanGraphs.
from pybaseball import batting_stats

# get all of this season's batting data so far
data = batting_stats(2017)
print("BATTING DATA FROM FANGRAPHS FOR THE SEASON")
print(data)

# retrieve data on only players who have 50+ plate appearances this year
data = batting_stats(2017, qual=50)
print("BATTING DATA FROM FANGRAPHS FOR THE SEASON WITH 50PA")
print(data)

# retrieve one row per player per season since 2000 (i.e.: who had the single most dominant season over this period?)
data = batting_stats(2010, 2016)
print("SEASON-LEVEL BATTING DATA FROM FANGRAPHS SINGLE ROW PER PLAYER PER SEASON")
print(data)

# retrieve aggregate player statistics from 2000 to 2016 (i.e.: who had the most home runs overall over this period?)
data = batting_stats(2010, 2016, ind=0)
print("SEASON-LEVEL BATTING DATA FROM FANGRAPHS AGGREGATE PLAYER STATS")
print(data)
print(data.columns.tolist())


# STATCAST BATTER
from pybaseball import statcast_batter
from pybaseball import playerid_lookup

# find David Ortiz's player id (mlbam_key)
playerid_lookup('ortiz','david')

# statcast_batter(start_dt=[yesterday's date], end_dt=None, player_id)
# get all available data
data = statcast_batter('2008-04-01', '2017-07-15', player_id = 120074)
print("STATCAST BATTER")
print(data)

# get data for July 15th, 2017
data = statcast_batter('2014-08-16', player_id = 120074)
print("STATCAST BATTER 8/16/2014")
print(data)
print(data.columns.tolist())

# STATCAST BATTER EXIT VELO BARRELS
# retrieves batted ball data for all batters in a given year.
from pybaseball import statcast_batter_exitvelo_barrels

# statcast_batter_exitvelo_barrels(year, minBBE=[qualified])
# minBBE: The minimum number of batted ball against events for each pitcher. 
# If a player falls below this threshold, they will be excluded from the results. 
# If no value is specified, only qualified batters will be returned.
# get data for all qualified batters in 2019
data = statcast_batter_exitvelo_barrels(2019)
print("STATCAST BATTER EXIT VELO BARRELS 2019")
print(data)

# get data for batters with a minimum of 100 batted ball events in 2019
data = statcast_batter_exitvelo_barrels(2019, 100)
print("STATCAST BATTER EXIT VELO BARRELS 2019 MIN 100PA")
print(data)
print(data.columns.tolist())

# STATCAST BATTER EXPECTED STATS
from pybaseball import statcast_batter_expected_stats

# statcast_batter_expected_stats(year, minPA=[qualified])
# minPA: The minimum number of plate appearances against for each player. 
# If a player falls below this threshold, they will be excluded from the results. 
# If no value is specified, only qualified batters will be returned.
# get data for all qualified batters in 2019
data = statcast_batter_expected_stats(2019)
print("STATCAST BATTER EXPECTED STATS 2019")
print(data)

# get data for batters with a minimum of 150 plate appearances against in 2019
data = statcast_batter_expected_stats(2019, 150)
print("STATCAST BATTER EXPECTED STATS 2019 MIN 150PA")
print(data)
print(data.columns.tolist())


# STATCAST BATTER PERCENTILE RANKS
#retrieves percentile ranks for each player in a given year, including batters with 
# 2.1 PA per team game and 1.25 for pitchers.
from pybaseball import statcast_batter_percentile_ranks

# statcast_batter_percentile_ranks(year)
# get data for all qualified batters in 2019
data = statcast_batter_percentile_ranks(2019)
print("STATCAST BATTER PERCENTILE RANKS")
print(data)
print(data.columns.tolist())


# STATCAST BATTER PITCH ARSENAL
from pybaseball import statcast_batter_pitch_arsenal

# statcast_pitcher_pitch_arsenal(2019, minP=[qualified], arsenal_type="average_speed")
# arsenal_type: The type of stat to retrieve for the batters' arsenals. Options include 
# ["average_speed", "n_", "average_spin"], where "n_" corresponds to the percentage share 
# for each pitch. If no value is specified, it will default to average speed.
# get average pitch speed data for all qualified batters in 2019
data = statcast_batter_pitch_arsenal(2019)
print("STATCAST BATTER PITCH ARSENAL 2019")
print(data)

# get data for batters with a minimum of 100 plate appearances in 2019
data = statcast_batter_pitch_arsenal(2019, 100)
print("STATCAST BATTER PITCH ARSENAL 2019 MIN 100PA")
print(data)
print(data.columns.tolist())