from .constants import *


class PlayerMatch:
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
		self.skill_int = data['skill']


	def skill(self):
		return ('Normal' if self.skill_int == 1 else 'High' if self.skill_int == 2 else 'Very High') + ' Skill'


	def mode(self):
		return kMODES[self.game_mode]


	def hero(self):
		return kHEROES[self.hero_id]


	def status(self):
		return 'ABANDON' if self.leaver_status > 1 else 'WON' if self.player_slot < 128 and self.radiant_win else 'LOST'


	def __str__(self):
		return '{}  {:15}  {:22}  {:20}  {:>2d}/{:>2d}/{:>2d}  {:7}'.format(self.match_id,
																			self.skill(),
																			self.mode(),
																			self.hero(),
																			self.kills,
																			self.deaths,
																			self.assists,
																			self.status())