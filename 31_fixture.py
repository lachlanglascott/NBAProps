# specify the start date is 2021 jan 1 st
# specify the emd date is 2021 feb 1 st
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
nba_teams_df = pd.DataFrame(nba_teams).rename(columns={"id": "TeamID", "full_name": "TeamName", "nickname": "TeamNickname", "city": "TeamCity", "state": "TeamState", "year_founded": "YearFounded"})

from nba_api.stats.endpoints import scoreboard

date_df = pd.DataFrame([])
  
for date_var in reg_season_date_22_23:
  
  date_data = scoreboard.Scoreboard(
  #day_offset=0,
  game_date=date_var,
  league_id = nba_id).get_data_frames()[0]
  
  date_df = date_df.append(date_data)
  
  print(f"Collected fixture for {date_var}")
  time.sleep(.600)

team_id_name = nba_teams_df[["TeamID", "TeamName", "abbreviation"]]

fixture = date_df.merge(team_id_name, left_on='HOME_TEAM_ID', right_on = 'TeamID', how='left', indicator=False) \
  .rename({'TeamName': 'HOME_TEAM_NAME', 'abbreviation': 'HOME_TEAM_ABBREVIATION'}, axis=1) \
  .merge(team_id_name, left_on='VISITOR_TEAM_ID', right_on = 'TeamID', how='left', indicator=False) \
  .rename({'TeamName': 'VISITOR_TEAM_NAME', 'abbreviation': 'VISITOR_TEAM_ABBREVIATION'}, axis=1)

  #define columns to move to front
  #cols_to_move = ['date', 'season', 'season_type', 'PLAYER_ID',  'PLAYER_NAME', 'starter_bench']

  #move columns to front
  #full_df =full_df[cols_to_move + [x for x in full_df.columns if x not in cols_to_move]]
  #full_df.columns= full_df.columns.str.lower()
  
  #view updated DataFrame
  print(fixture)

fixture.to_sql('bronze_fixture_22_23', con = engine, if_exists = 'replace', index = False, index_label=None)     

#db_roster_df = pd.read_sql("""select  * from fixture_22_23""",con)
#db_roster_df

