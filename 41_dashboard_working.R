#### Player Team tables
assists_tbl <- dashboard_data %>%
  dplyr::arrange(desc(date)) %>%
  dplyr::group_by(player_name) %>%
  dplyr::mutate(row_number = row_number()) %>%
  dplyr::summarise(games_played = dplyr::n(),
                   # POTENTIAL ASSISTS
                   potential_assists_l1 = sum(potential_ast[row_number <= 1]),
                   potential_assists_l3 = sum(potential_ast[row_number <= 3]),
                   potential_assists_l5 = sum(potential_ast[row_number <= 5]),
                   potential_assists_l7 = sum(potential_ast[row_number <= 7]),
                   potential_assists_season = sum(potential_ast),
                   # ASSISTS
                   assists_l1 = sum(ast[row_number <= 1]),
                   assists_l3 = sum(ast[row_number <= 3]),
                   assists_l5 = sum(ast[row_number <= 5]),
                   assists_l7 = sum(ast[row_number <= 7]),
                   assists_season = sum(ast),
                   ) %>%
  dplyr::ungroup() %>%
  dplyr::mutate(# POTENTIAL ASSISTS
                potential_assists_l1 = ifelse(games_played >=1, potential_assists_l1/1, NA),
                potential_assists_l3 = ifelse(games_played >=3, potential_assists_l3/3, NA),
                potential_assists_l5 = ifelse(games_played >=5, potential_assists_l5/5, NA),
                potential_assists_l7 = ifelse(games_played >=7, potential_assists_l7/7, NA),
                
                # ASSISTS
                assists_l1 = ifelse(games_played >=1, assists_l1/1, NA),
                assists_l3 = ifelse(games_played >=3, assists_l3/3, NA),
                assists_l5 = ifelse(games_played >=5, assists_l5/5, NA),
                assists_l7 = ifelse(games_played >=7, assists_l7/7, NA))

rebounds_tbl <- dashboard_data %>%
  dplyr::arrange(desc(date)) %>%
  dplyr::group_by(player_name) %>%
  dplyr::mutate(row_number = row_number()) %>%
  dplyr::summarise(games_played = dplyr::n(),
                   # POTENTIAL rebounds
                   potential_rebounds_l1 = sum(potential_ast[row_number <= 1]),
                   potential_rebounds_l3 = sum(potential_ast[row_number <= 3]),
                   potential_rebounds_l5 = sum(potential_ast[row_number <= 5]),
                   potential_rebounds_l7 = sum(potential_ast[row_number <= 7]),
                   potential_rebounds_season = sum(potential_ast),
                   # rebounds
                   rebounds_l1 = sum(ast[row_number <= 1]),
                   rebounds_l3 = sum(ast[row_number <= 3]),
                   rebounds_l5 = sum(ast[row_number <= 5]),
                   rebounds_l7 = sum(ast[row_number <= 7]),
                   rebounds_season = sum(ast),
  ) %>%
  dplyr::ungroup() %>%
  dplyr::mutate(# POTENTIAL rebounds
    potential_rebounds_l1 = ifelse(games_played >=1, potential_rebounds_l1/1, NA),
    potential_rebounds_l3 = ifelse(games_played >=3, potential_rebounds_l3/3, NA),
    potential_rebounds_l5 = ifelse(games_played >=5, potential_rebounds_l5/5, NA),
    potential_rebounds_l7 = ifelse(games_played >=7, potential_rebounds_l7/7, NA),
    
    # rebounds
    rebounds_l1 = ifelse(games_played >=1, rebounds_l1/1, NA),
    rebounds_l3 = ifelse(games_played >=3, rebounds_l3/3, NA),
    rebounds_l5 = ifelse(games_played >=5, rebounds_l5/5, NA),
    rebounds_l7 = ifelse(games_played >=7, rebounds_l7/7, NA)) 




# COMBINED TABLE
#### Player Team tables
assists_tbl <- dashboard_data %>%
  dplyr::arrange(desc(date)) %>%
  dplyr::group_by(player_name) %>%
  dplyr::mutate(row_number = row_number()) %>%
  dplyr::summarise(games_played = dplyr::n(),
                   # POTENTIAL ASSISTS
                   potential_assists_l1 = sum(potential_ast[row_number <= 1]),
                   potential_assists_l3 = sum(potential_ast[row_number <= 3]),
                   potential_assists_l5 = sum(potential_ast[row_number <= 5]),
                   potential_assists_l7 = sum(potential_ast[row_number <= 7]),
                   potential_assists_season = sum(potential_ast),
                   # ASSISTS
                   assists_l1 = sum(ast[row_number <= 1]),
                   assists_l3 = sum(ast[row_number <= 3]),
                   assists_l5 = sum(ast[row_number <= 5]),
                   assists_l7 = sum(ast[row_number <= 7]),
                   assists_season = sum(ast),
  ) %>%
  dplyr::ungroup() %>%
  dplyr::mutate(# POTENTIAL ASSISTS
    potential_assists_l1 = ifelse(games_played >=1, potential_assists_l1/1, NA),
    potential_assists_l3 = ifelse(games_played >=3, potential_assists_l3/3, NA),
    potential_assists_l5 = ifelse(games_played >=5, potential_assists_l5/5, NA),
    potential_assists_l7 = ifelse(games_played >=7, potential_assists_l7/7, NA),
    
    # ASSISTS
    assists_l1 = ifelse(games_played >=1, assists_l1/1, NA),
    assists_l3 = ifelse(games_played >=3, assists_l3/3, NA),
    assists_l5 = ifelse(games_played >=5, assists_l5/5, NA),
    assists_l7 = ifelse(games_played >=7, assists_l7/7, NA))

rebounds_tbl <- dashboard_data %>%
  dplyr::arrange(desc(date)) %>%
  dplyr::group_by(player_name) %>%
  dplyr::mutate(row_number = row_number()) %>%
  dplyr::summarise(games_played = dplyr::n(),
                   # POTENTIAL rebounds
                   potential_rebounds_l1 = sum(potential_ast[row_number <= 1]),
                   potential_rebounds_l3 = sum(potential_ast[row_number <= 3]),
                   potential_rebounds_l5 = sum(potential_ast[row_number <= 5]),
                   potential_rebounds_l7 = sum(potential_ast[row_number <= 7]),
                   potential_rebounds_season = sum(potential_ast),
                   # rebounds
                   rebounds_l1 = sum(ast[row_number <= 1]),
                   rebounds_l3 = sum(ast[row_number <= 3]),
                   rebounds_l5 = sum(ast[row_number <= 5]),
                   rebounds_l7 = sum(ast[row_number <= 7]),
                   rebounds_season = sum(ast),
  ) %>%
  dplyr::ungroup() %>%
  dplyr::mutate(# POTENTIAL rebounds
    potential_rebounds_l1 = ifelse(games_played >=1, potential_rebounds_l1/1, NA),
    potential_rebounds_l3 = ifelse(games_played >=3, potential_rebounds_l3/3, NA),
    potential_rebounds_l5 = ifelse(games_played >=5, potential_rebounds_l5/5, NA),
    potential_rebounds_l7 = ifelse(games_played >=7, potential_rebounds_l7/7, NA),
    
    # rebounds
    rebounds_l1 = ifelse(games_played >=1, rebounds_l1/1, NA),
    rebounds_l3 = ifelse(games_played >=3, rebounds_l3/3, NA),
    rebounds_l5 = ifelse(games_played >=5, rebounds_l5/5, NA),
    rebounds_l7 = ifelse(games_played >=7, rebounds_l7/7, NA)) 


#### Player Team tables


all_player_tbl <- dashboard_data %>%
  dplyr::arrange(desc(date)) %>%
  dplyr::group_by(player_name) %>%
  dplyr::mutate(row_number = row_number()) %>%
  dplyr::summarise(games_played = dplyr::n(),
                   
                   #FG%
                   eff_fg_pct_l1 = mean(eff_fg_pct[row_number <= 1]),
                   eff_fg_pct_l3 = mean(eff_fg_pct[row_number <= 3]),
                   eff_fg_pct_l5 = mean(eff_fg_pct[row_number <= 5]),
                   eff_fg_pct_l7 = mean(eff_fg_pct[row_number <= 7]),
                   eff_fg_pct_season = mean(eff_fg_pct),
                   
                   # points
                   points_l1 = sum(points[row_number <= 1]),
                   points_l3 = sum(points[row_number <= 3]),
                   points_l5 = sum(points[row_number <= 5]),
                   points_l7 = sum(points[row_number <= 7]),
                   points_season = sum(points),
                   
                   # POTENTIAL ASSISTS
                   potential_assists_l1 = sum(potential_ast[row_number <= 1]),
                   potential_assists_l3 = sum(potential_ast[row_number <= 3]),
                   potential_assists_l5 = sum(potential_ast[row_number <= 5]),
                   potential_assists_l7 = sum(potential_ast[row_number <= 7]),
                   potential_assists_season = sum(potential_ast),
                   
                   # ASSISTS
                   assists_l1 = sum(ast[row_number <= 1]),
                   assists_l3 = sum(ast[row_number <= 3]),
                   assists_l5 = sum(ast[row_number <= 5]),
                   assists_l7 = sum(ast[row_number <= 7]),
                   assists_season = sum(ast),
                   
                  # POTENTIAL rebounds
                   potential_rebounds_l1 = sum(potential_ast[row_number <= 1]),
                   potential_rebounds_l3 = sum(potential_ast[row_number <= 3]),
                   potential_rebounds_l5 = sum(potential_ast[row_number <= 5]),
                   potential_rebounds_l7 = sum(potential_ast[row_number <= 7]),
                   potential_rebounds_season = sum(potential_ast),
                   # rebounds
                   rebounds_l1 = sum(ast[row_number <= 1]),
                   rebounds_l3 = sum(ast[row_number <= 3]),
                   rebounds_l5 = sum(ast[row_number <= 5]),
                   rebounds_l7 = sum(ast[row_number <= 7]),
                   rebounds_season = sum(ast),
  ) %>%
  dplyr::ungroup() %>%
  dplyr::mutate(
    
    # POINTS
    points_l1 = ifelse(games_played >=1, points_l1/1, NA),
    points_l3 = ifelse(games_played >=3, points_l3/3, NA),
    points_l5 = ifelse(games_played >=5, points_l5/5, NA),
    points_l7 = ifelse(games_played >=7, points_l7/7, NA),
    
    
    # POTENTIAL ASSISTS
    potential_assists_l1 = ifelse(games_played >=1, potential_assists_l1/1, NA),
    potential_assists_l3 = ifelse(games_played >=3, potential_assists_l3/3, NA),
    potential_assists_l5 = ifelse(games_played >=5, potential_assists_l5/5, NA),
    potential_assists_l7 = ifelse(games_played >=7, potential_assists_l7/7, NA),
    
    # ASSISTS
    assists_l1 = ifelse(games_played >=1, assists_l1/1, NA),
    assists_l3 = ifelse(games_played >=3, assists_l3/3, NA),
    assists_l5 = ifelse(games_played >=5, assists_l5/5, NA),
    assists_l7 = ifelse(games_played >=7, assists_l7/7, NA),
    
    potential_rebounds_l1 = ifelse(games_played >=1, potential_rebounds_l1/1, NA),
    potential_rebounds_l3 = ifelse(games_played >=3, potential_rebounds_l3/3, NA),
    potential_rebounds_l5 = ifelse(games_played >=5, potential_rebounds_l5/5, NA),
    potential_rebounds_l7 = ifelse(games_played >=7, potential_rebounds_l7/7, NA),
    
    # rebounds
    rebounds_l1 = ifelse(games_played >=1, rebounds_l1/1, NA),
    rebounds_l3 = ifelse(games_played >=3, rebounds_l3/3, NA),
    rebounds_l5 = ifelse(games_played >=5, rebounds_l5/5, NA),
    rebounds_l7 = ifelse(games_played >=7, rebounds_l7/7, NA)
)

# POTENTIAL ASSIST

#### FIXTURE AND ROSTER

names(fixture_22_23)
names(roster_live)
names(dashboard_data)


#### Last Year
#Use dashboard data team abbreviation (no change)

#### This year
#Use roster data

#### Daily Matchups
#New tab








                
