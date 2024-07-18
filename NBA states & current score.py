from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()


def get_links():
  data = get(BASE_URl + ALL_JSON).json()
  links = data['links']
  return links


def get_scoreboard():
  scoreboard = get_links()['currentScoreboard']
  data = get(BASE_URL + scoreboard).json()['games']
  
  for game in games:
    home_team = game['hTeam']
    away_team = game['vteam']
    clock = game['clock']
    period = game['period']
    
    
    print('______________________________')
    print(f"{home_team['tricode']} vs {away_team['tricode']}, {clock},{period}")
    print(f"{home_team['score]} - {away_team['score]}")
    print(f{}"{clock} - {period}['current']}")
    printer.pprint(games.keys())
  
  printer.pprint(data.keys())
print('get_links()')