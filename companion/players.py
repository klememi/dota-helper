from .helpers import *
from .constants import *
from .player import Player


pro_players_endpoint    = '/proPlayers'
player_endpoint         = '/players/{}'
win_loss_endpoint       = '/players/{}/wl'
recent_matches_endpoint = '/players/{}/recentMatches'
heroes_endpoint         = '/players/{}/heroes'
counts_endpoint         = '/players/{}/counts'
totals_endpoint         = '/players/{}/totals'
peers_endpoint          = '/players/{}/peers'
team_filter             = ['team_name', 'team_tag']
country_filter          = ['loccountrycode', 'country_code']
name_filter             = ['personaname', 'name']


def players_favourite():
	pass


def players_id(id_):
	try:
		data_player = get_response_json(player_endpoint.format(id_))
		data_wl = get_response_json(win_loss_endpoint.format(id_))
		data_counts = get_response_json(counts_endpoint.format(id_))
		data_general = {**data_player, **data_wl, **data_counts}
		data_matches = get_response_json(recent_matches_endpoint.format(id_))
		data_heroes = get_response_json(heroes_endpoint.format(id_))
		data_totals = get_response_json(totals_endpoint.format(id_))
		data_peers = get_response_json(peers_endpoint.format(id_))
		player = Player(data_general, data_matches, data_heroes, data_totals, data_peers)
	except Exception as err:
		return print(err)
	print(player)


def process_players(data, country, team, name):
	if country: data = filter_substr(country_filter, country, data)
	if team:    data = filter_substr(team_filter, team, data)
	if name:    data = filter_substr(name_filter, name, data)
	data.sort(key=lambda a: a['name'].lower())
	print_players(data)


def print_players(data):
	if not data: return print(kNO_DATA)
	print('{:30} {:7} {:30} {:10}'.format('Name', 
									      'Country',
									      'Team',
									      'ID'))
	print(80 * '-')
	for p in data:
		print('{:30} {:7} {:30} {:<10}'.format(p['name'] or p['personaname'] or kUNKNOWN, 
											   p['loccountrycode'] or p['country_code'].upper() or kUNKNOWN, 
											   p['team_name'] or kUNKNOWN,
											   p['account_id'] or kUNKNOWN))
