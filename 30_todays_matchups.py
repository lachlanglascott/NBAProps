from nba_api.stats.endpoints import scoreboard

tomorrow_data = scoreboard.Scoreboard(
  #day_offset=0,
  game_date=tomorrow_date,
  league_id = nba_id).get_data_frames()[0]

tomorrow_data.columns

team_id_name = nba_teams_df[["id", "full_name"]]

matchups = tomorrow_data.merge(team_id_name, left_on='HOME_TEAM_ID', right_on = 'id', how='left', indicator=True) \
  .rename({'full_name': 'HOME_TEAM_NAME'}, axis=1)  \
  .merge(team_id_name, left_on='AWAY_TEAM_ID', right_on = 'id', how='left', indicator=True) 
  


# from nba_api.stats.endpoints import teamgamelog
# 
# data = teamgamelog.TeamGameLog(
#         team_id = '1610612753',
#         season = Season.current_season,
#         season_type_all_star=SeasonType.default).get_data_frames()[0]



