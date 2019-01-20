from .constants import *


class Player:
	def __init__(self, data_general, data_matches, data_heroes, data_totals, data_peers):
		self.name = data_general['profile']['name'] or data_general['profile']['personaname'] or kUNKNOWN
		self.country = data_general['profile']['loccountrycode'] or kUNKNOWN
		self.mmr = data_general['mmr_estimate']['estimate']
		self.rank = data_general['rank_tier']
		self.leaderboard_rank = data_general['leaderboard_rank']
		self.win = data_general['win']
		self.lose = data_general['lose']
		self.recent_matches = [PlayerMatch(data_match) for data_match in data_matches[:5]]
		best_heroes_data = list(filter(lambda a: a['games'] > 20, data_heroes))
		best_heroes_data.sort(key=lambda a: a['win'] / a['games'])
		self.heroes_best = [PlayerHero(data_hero) for data_hero in best_heroes_data[:3]]
		scariest_heroes_data = list(filter(lambda a: a['against_games'] > 20, data_heroes))
		scariest_heroes_data.sort(key=lambda a: a['against_win'] / a['against_games'], reverse=True)
		self.heroes_scariest = [PlayerHero(data_hero) for data_hero in scariest_heroes_data[:3]]
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
		self.best_friends = [PlayerFriend(data_friend) for data_friend in friends_data[:3]]


	def __str__(self):
		return (''
				''
				''
				'').format()
