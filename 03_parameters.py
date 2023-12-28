#### NBA League ID
from nba_api.stats.library.parameters import LeagueID
nba_id = LeagueID.nba

#### Season IDs
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType

#### Date Ranges
from datetime import date
from datetime import timedelta
import time

# Today
today_date = date.today()
print(today_date)

# Yesterday
yesterday_date = date.today()  - timedelta(days=1)
#yesterday_date = today.strftime("%m-%d-%Y")
print(yesterday_date)

# Tomorrow
tomorrow_date = date.today() + timedelta(days=1)
#yesterday_date = today.strftime("%m-%d-%Y")
print(tomorrow_date)

# specify the start date is 2021 jan 1 st
# specify the emd date is 2021 feb 1 st
reg_season_date_21_22 = pd.date_range(start='10-19-2021', end='04-10-2022').strftime("%m-%d-%Y")
reg_season_date_21_22

reg_season_date_22_23 = pd.date_range(start='10-18-2022', end='04-09-2023').strftime("%m-%d-%Y")
reg_season_to_date_22_23 = pd.date_range(start='10-18-2022', end=today_date.strftime("%m-%d-%Y")).strftime("%m-%d-%Y")

# Missing dates from database
#pd.read_sql("""select * from nba_player_measures limit 100'""",con)
database_date_range_22_23 = pd.read_sql("""select distinct date from nba_player_measures where season = '2022'""",con)
database_date_range_22_23

database_missing_dates_22_23 = (reg_season_date_22_23.to_frame(index=False, name = 'date') \
  .merge(database_date_range_22_23, on='date', how='outer', indicator=True) \
  .query('_merge != "both"') \
  .drop(columns='_merge')
   )
database_missing_dates_22_23


from nba_api.stats.endpoints import playercareerstats

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

from nba_api.stats.static import players
player_dict = players.get_players()

# Use ternary operator or write function 
# Names are case sensitive
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

# find team Ids
from nba_api.stats.static import teams 
teams = teams.get_teams()
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

# First we import the endpoint
# We will be using pandas dataframes to manipulate the data
from nba_api.stats.endpoints import playergamelog
import pandas as pd 

#Call the API endpoint passing in lebron's ID & which season 
gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season = '2018')

#Converts gamelog object into a pandas dataframe
#can also convert to JSON or dictionary  
df_bron_games_2018 = gamelog_bron.get_data_frames()

# If you want all seasons, you must import the SeasonAll parameter 
from nba_api.stats.library.parameters import SeasonAll

gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)

df_bron_games_all = gamelog_bron_all.get_data_frames()





from nba_api.stats.endpoints import commonplayerinfo

# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)


custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Only available after v1.1.0
# Proxy Support, Custom Headers Support, Timeout Support (in seconds)
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544, proxy='127.0.0.1:80', headers=custom_headers, timeout=100)

