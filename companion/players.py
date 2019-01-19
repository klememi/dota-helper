from .helpers import *


pro_players_endpoint = '/proPlayers'
team_filter          = ['team_name', 'team_tag']
country_filter       = ['loccountrycode', 'country_code']
name_filter          = ['personaname', 'name']


def players_favourite():
	pass


def players_id(id_):
	pass


def process_players(data, country, team, name):
	if country: data = filter_substr(country_filter, country, data)
	if team:    data = filter_substr(team_filter, team, data)
	if name:    data = filter_substr(name_filter, name, data)
	print_players(data)


def print_players(data):
	if not data: return print('Data matching your criteria not found.')
	print('{:20} {:7} {:20} {:7} {:10}'.format('Name', 'Country', 'Team', 'Role', 'ID'))
	print(70 * '-')
	for p in data:
		print('{:20} {:7} {:20} {:<7} {:<10}'.format(p['name'] or p['personaname'] or '', p['loccountrycode'] or p['country_code'].upper(), p['team_name'] or '', p['fantasy_role'], p['account_id']))
