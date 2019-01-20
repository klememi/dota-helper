class PlayerHero:
	def __init__(self, data):
		self.hero_id = data['hero_id']
		self.games = data['games']
		self.win = data['win']
		self.against_games = data['against_games']
		self.against_wins = data['against_win']
