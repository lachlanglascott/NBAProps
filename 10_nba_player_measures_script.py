from nba_api.stats.endpoints import leaguedashptstats
from nba_api.stats.library.parameters import StarterBench

# PARAMETERS DEFINED IN 03_PARAMETERS

seasontype = SeasonType.preseason

def scrape_data(date_var):
  
  starter_vars = [StarterBench.starters, StarterBench.bench]
  measure_vars = ["Passing", "Rebounding", "Efficiency"]
  
  #### PASSING #### 

  df_list = []
    
  for measure_var in measure_vars:
    df = pd.DataFrame([]) 
  
    for starter_var in starter_vars:
      print(f"Fetching {measure_var} data from {starter_var}")
      data = leaguedashptstats.LeagueDashPtStats(
        pt_measure_type = measure_var,
        player_or_team ="Player",
        date_from_nullable = date_var, #MM/DD/YYYY
        date_to_nullable = date_var, #MM/DD/YYYY
        # last_n_games = 1,
        starter_bench_nullable = starter_var,
        season = Season.default,
        season_type_all_star = seasontype).get_data_frames()[0]
    
      data = data.assign(
        starter_bench = starter_var
  )
      df = df.append(data)
      print(f"Collected {measure_var} {starter_var} Data")
    df_list.append(df)
    print(f"Appended List")

  full_df = df_list[0] \
  .merge(df_list[1],on=['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'GP', 'W', 'L', 'MIN', 'starter_bench']) \
  .merge(df_list[2],on=['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'GP', 'W', 'L', 'MIN', 'starter_bench']) \
  .assign(
      season_type =  seasontype,
      season = Season.default,
      date = date_var
      )

  list(full_df.columns)

  #define columns to move to front
  cols_to_move = ['date', 'season', 'season_type', 'PLAYER_ID',  'PLAYER_NAME', 'starter_bench']

  #move columns to front
  full_df =full_df[cols_to_move + [x for x in full_df.columns if x not in cols_to_move]]
  full_df.columns= full_df.columns.str.lower()

  #view updated DataFrame
  #print(full_df)
  return full_df

df = scrape_data(date_var=yesterday_date)

df
