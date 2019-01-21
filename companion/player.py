from .constants import *
from .helpers import *
from .player_match import PlayerMatch
from .player_hero import PlayerHero
from .player_friend import PlayerFriend


class Player:
	'''
	Player entity holding important data for the player.
	'''


	def __init__(self, data_general, data_matches, data_heroes, data_totals, data_peers):
		self.name = data_general['profile']['name'] or data_general['profile']['personaname'] or kUNKNOWN
		self.country = data_general['profile']['loccountrycode'] or kUNKNOWN
		self.mmr = data_general['mmr_estimate']['estimate']
		self.rank = data_general['rank_tier']
		self.leaderboard_rank = data_general['leaderboard_rank']
		self.win = data_general['win']
		self.lose = data_general['lose']
		self.recent_matches = [PlayerMatch(data_match) for data_match in data_matches[:5]]
		best_heroes_data = list(filter(lambda a: a['games'] > 30, data_heroes))
		best_heroes_data.sort(key=lambda a: a['win'] / a['games'], reverse=True)
		self.heroes_best = [PlayerHero(data_hero, True) for data_hero in best_heroes_data[:3]]
		scariest_heroes_data = list(filter(lambda a: a['against_games'] > 30, data_heroes))
		scariest_heroes_data.sort(key=lambda a: a['against_win'] / a['against_games'])
		self.heroes_scariest = [PlayerHero(data_hero, False) for data_hero in scariest_heroes_data[:3]]
		self.radiant_games = data_general['is_radiant']['1']['games']
		self.radiant_wins = data_general['is_radiant']['1']['win']
		self.dire_games = data_general['is_radiant']['0']['games']
		self.dire_wins = data_general['is_radiant']['0']['win']
		data_kda = filter_eq(['field'], 'kda', data_totals)[0]
		self.kda = data_kda['sum'] / data_kda['n']
		data_courier_kills = filter_eq(['field'], 'courier_kills', data_totals)[0]
		self.courier_kills = data_courier_kills['sum']
		friends_data = list(filter(lambda a: a['games'] > 30, data_peers))
		friends_data.sort(key=lambda a: a['win'] / a['games'], reverse=True)
		self.best_friends = [PlayerFriend(data_friend) for data_friend in friends_data[:3]]


	def prefers(self):
		'''
		Defines which side player prefers.

		:return: Side name.
		'''
		radiant_ratio = self.radiant_wins / self.radiant_games
		dire_ratio = self.dire_wins / self.dire_games
		return 'Radiant' if radiant_ratio > dire_ratio else 'Dire'


	def __str__(self):
		return ('{}, {}\n'
				'{} ({} MMR)\n'
				'Win: {}  Loss: {}\n'
				'Prefers: {}\n'
				'Avg KDA: {:3.1f}\n'
				'Courier kills: {}\n'
				'# RECENT MATCHES\n'
				'{}'
				'\n# BEST HEROES\n'
				'{}'
				'\n# SCARIEST HEROES\n'
				'{}'
				'\n# BEST FRIENDS\n'
				'{}').format(self.name,
							 self.country.upper(),
							 kRANKS[self.rank] if self.rank else kUNKNOWN,
							 self.mmr,
							 self.win,
							 self.lose,
							 self.prefers(),
							 self.kda,
							 self.courier_kills,
							 '\n'.join([m.__str__() for m in self.recent_matches]),
							 '\n'.join([h.__str__() for h in self.heroes_best]),
							 '\n'.join([h.__str__() for h in self.heroes_scariest]),
							 '\n'.join([f.__str__() for f in self.best_friends]))
