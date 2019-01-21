class PlayerFriend:
	'''
	Entity holding important data for player's best friends data.
	'''

	def __init__(self, data):
		self.name = data['personaname']
		self.account_id = data['account_id']
		self.games = data['games']
		self.win = data['win']


	def __str__(self):
		return '{:30} ({})  Games: {:>4d}  Win: {:5.1f} %'.format(self.name,
															      self.account_id,
															      self.games,
															      100 * self.win / self.games)
