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
		self.skill = data['skill']
