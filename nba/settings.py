from pymongo import MongoClient

MONGO_CLIENT = MongoClient('mongodb://localhost:27017/')
NBA_DB = MONGO_CLIENT['nba_db']
PLAYERS_TRADITIONAL = NBA_DB['players_traditional']
PLAYERS_ADVANCED = NBA_DB['players_advanced']
TEAMS_ADVANCED = NBA_DB['teams_advanced']

URLS = {
    'players_traditional': "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1",
    'players_advanced': "https://www.nba.com/stats/players/advanced",
    'teams_advanced': "https://www.nba.com/stats/teams/advanced"
}

HEADERS = {
    'players_traditional': ['Player','Team','Age','GP','W','L','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','TOV','STL','BLK','PF','FP','DD2','TD3','+/-'],
    'players_advanced': ['Player','Team','Age','GP','W','L','MIN','OFFRTG','DEFRTG','NETRTG','AST%','AST/TO','AST RATIO','OREB%','DREB%','REB%','TO RATIO','EFG%','TS%','USG%','PACE','PIE', 'POSS'],
    'teams_advanced': ['Team','GP','W','L','MIN','OFFRTG','DEFRTG','NETRTG','AST%','AST/TO','AST RATIO','OREB%','DREB%','REB%','TO RATIO','EFG%','TS%','PACE','PIE','POSS']
}