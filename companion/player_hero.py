from .constants import *


class PlayerHero:
	def __init__(self, data, best):
		self.hero_id = data['hero_id']
		self.games = data['games']
		self.win = data['win']
		self.against_games = data['against_games']
		self.against_wins = data['against_win']
		self.best = best


	def best_hero_str(self):
		return '{:20}  Games: {:>4d}  Won: {:5.1f} %'.format(kHEROES[int(self.hero_id)],
													         self.games,
													         100 * self.win / self.games)


	def scariest_hero_str(self):
		return '{:20}  Against: {:>4d}  Lost: {:5.1f} %'.format(kHEROES[int(self.hero_id)],
															    self.against_games,
															    100 * (1 - (self.against_wins / self.against_games)))


	def __str__(self):
		if self.best: return self.best_hero_str()
		return self.scariest_hero_str()
