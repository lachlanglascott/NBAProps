from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
nba_teams_df = pd.DataFrame(nba_teams).rename(columns={"id": "TeamID", "full_name": "TeamName", "nickname": "TeamNickname", "city": "TeamCity", "state": "TeamState", "year_founded": "YearFounded"})

teams = pd.DataFrame(nba_teams, columns = ['id']).values.tolist()

roster_df = pd.DataFrame([])  
  for team in teams:
      
    roster_data = commonteamroster.CommonTeamRoster(
      team_id = team,
      season = Season.default).get_data_frames()[0]
    
    roster_df = roster_df.append(roster_data)
    print(f"Collected Data")
    time.sleep(.600)
    
roster_df_team_names = roster_df.merge(nba_teams_df, on='TeamID',  how='left', indicator=True)

#roster_df_team_names.columns= roster_df_team_names.columns.str.lower()

roster_df_team_names.to_sql('bronze_rosters_live', con = engine, if_exists = 'replace', index = False, index_label=None)     


#db_roster_df = pd.read_sql("""select  * from roster_live""",con)
#db_roster_df

