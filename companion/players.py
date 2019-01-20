from .helpers import *


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
	print_players(data)


def print_players(data):
	if not data: return print('Data matching your criteria not found.')
	print('{:20} {:7} {:20} {:10}'.format('Name', 
									      'Country',
									      'Team',
									      'ID'))
	print(70 * '-')
	for p in data:
		print('{:20} {:7} {:20} {:<10}'.format(p['name'] or p['personaname'] or 'unknown', 
											   p['loccountrycode'] or p['country_code'].upper(), 
											   p['team_name'] or 'unknown',
											   p['account_id']))


class Player:
	def __init__(self, data_general, data_matches, data_heroes, data_totals, data_peers):
		self.name = data_general['profile']['name'] or data_general['profile']['personaname'] or 'unknown'
		self.country = data_general['profile']['loccountrycode'] or 'unknown'
		self.mmr = data_general['mmr_estimate']['estimate']
		self.rank = data_general['rank_tier']
		self.leaderboard_rank = data_general['leaderboard_rank']
		self.win = data_general['win']
		self.lose = data_general['lose']
		self.recent_matches = [Match(data_match) for data_match in data_matches[:5]]
		best_heroes_data = list(filter(lambda a: a['games'] > 20, data_heroes))
		best_heroes_data.sort(key=lambda a: a['win'] / a['games'])
		self.heroes_best = [Hero(data_hero) for data_hero in best_heroes_data[:3]]
		scariest_heroes_data = list(filter(lambda a: a['against_games'] > 20, data_heroes))
		scariest_heroes_data.sort(key=lambda a: a['against_win'] / a['against_games'], reverse=True)
		self.heroes_scariest = [Hero(data_hero) for data_hero in scariest_heroes_data[:3]]
		self.radiant_games = data_general['is_radiant']['1']['games']
		self.radiant_wins = data_general['is_radiant']['1']['win']
		self.dire_games = data_general['is_radiant']['0']['games']
		self.dire_wins = data_general['is_radiant']['0']['win']
		data_kda = filter_eq(['field'], 'kda', data_totals)[0]
		self.kda = data_kda['sum'] / data_kda['n']
		data_courier_kills = filter_eq(['field'], 'courier_kills', data_totals)[0]
		self.courier_kills = data_courier_kills['sum']
		friends_data = list(filter(lambda a: a['games'] > 20, data_peers))
		friends_data.sort(key=lambda a: a['win'] / a['games'])
		self.best_friends = [Friend(data_friend) for data_friend in friends_data[:3]]


	def __str__(self):
		return '{} {}'.format(self.name, self.country)


class Match:
	def __init__(self, data):
		self.match_id = data['match_id']
		self.game_mode = data['game_mode']
		self.leaver_status = data['leaver_status']
		self.kills = data['kills']
		self.deaths = data['deaths']
		self.assists = data['assists']
		self.hero_id = data['hero_id']
		self.start_time = data['start_time']
		self.duration = data['duration']
		self.player_slot = data['player_slot']
		self.radiant_win = data['radiant_win']
		self.skill = data['skill']


class Hero:
	def __init__(self, data):
		self.hero_id = data['hero_id']
		self.games = data['games']
		self.win = data['win']
		self.against_games = data['against_games']
		self.against_wins = data['against_win']


class Friend:
	def __init__(self, data):
		self.name = data['personaname']
		self.account_id = data['account_id']
		self.games = data['games']
		self.games = data['win']
