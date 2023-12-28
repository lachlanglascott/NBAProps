#### Read in tables
con = engine.connect()

# Stats
bronze_nba_player_measures_21_22_final = pd.read_sql("""select * from bronze_player_measures_21_22_final""",con)
#bronze_nba_player_measures_22_23_live = []
bronze_nba_player_measures_22_23_live = pd.read_sql("""select * from bronze_nba_player_measures_22_23""",con)

# Fixture
bronze_fixture_22_23 = pd.read_sql("""select * from bronze_fixture_22_23""",con)

# Roster
bronze_rosters_live = pd.read_sql("""select * from bronze_rosters_live""",con)


#### Create silver tables ####

#### Stats
silver_player_measures = bronze_nba_player_measures_21_22_final.append(bronze_nba_player_measures_22_23_live)
silver_player_measures['date'] = pd.to_datetime(silver_player_measures['date'], format='%m-%d-%Y')
silver_player_measures['date'] = pd.to_datetime(silver_player_measures['date']).dt.date

silver_player_measures.columns
silver_player_measures.head()

#### Fixture
bronze_fixture_22_23.columns
bronze_fixture_22_23.head()

bronze_fixture_22_23['date'] = pd.to_datetime(bronze_fixture_22_23['GAME_DATE_EST']).dt.date
bronze_fixture_22_23['season'] = bronze_fixture_22_23['SEASON'] + '-' + (bronze_fixture_22_23['SEASON'].str.slice(2, 4).astype(int) + 1).astype(str)
bronze_fixture_22_23 = bronze_fixture_22_23.drop(columns=['SEASON', 'TeamID_x', 'TeamID_y'])
bronze_fixture_22_23.columns = bronze_fixture_22_23.columns.str.lower()

silver_fixture_22_23 = bronze_fixture_22_23

#move columns to front
fixture_cols_to_move = ['date', 'season',  'home_team_name',  'visitor_team_name', 'game_sequence']
silver_fixture_22_23 = silver_fixture_22_23[fixture_cols_to_move + [x for x in silver_fixture_22_23.columns if x not in fixture_cols_to_move]]


#### Roster
bronze_rosters_live.columns
bronze_rosters_live.head()

bronze_rosters_live['season'] = bronze_rosters_live['SEASON'] + '-' + (bronze_rosters_live['SEASON'].str.slice(2, 4).astype(int) + 1).astype(str)
bronze_rosters_live = bronze_rosters_live.drop(columns=['SEASON', '_merge'])
bronze_rosters_live.columns = bronze_rosters_live.columns.str.lower()
bronze_rosters_live = bronze_rosters_live.rename(columns={"teamid": "team_id", "leagueid": "league_id", "player": "player_name", "nickname": "player_nickname", "num": "player_num", "position": "player_position", "teamname": "team_name", "abbreviation": "team_abbreviation", "teamnickname": "team_nickname", "teamcity": "team_city", "state": "team_state", "yearfounded": "team_year_founded"})
silver_rosters_live = bronze_rosters_live

#move columns to front
roster_cols_to_move =['season', 'team_name', 'team_abbreviation', 'player_name']
silver_rosters_live = silver_rosters_live[roster_cols_to_move + [x for x in silver_rosters_live.columns if x not in roster_cols_to_move]]



#### Save silver tables
silver_player_measures.to_sql('silver_player_measures', con = engine, if_exists = 'replace', index = False, index_label=None)   
silver_fixture_22_23.to_sql('silver_fixture_22_23', con = engine, if_exists = 'replace', index = False, index_label=None)    
silver_rosters_live.to_sql('silver_rosters_live', con = engine, if_exists = 'replace', index = False, index_label=None)   
