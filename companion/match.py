from enum import Enum
from .constants import *


class MatchType(Enum):
	'''
	Defines Match entity type.
	'''
	RECENT = 1
	LIVE   = 2
	EXACT  = 3


class Match:
	'''
	Match entity holding important data for the match.
	'''

	def __init__(self, data, type):
		self.type = type
		self.data = data


	def __str__(self):
		if not self.data: return kNO_DATA
		if self.type == MatchType.RECENT: return self.matches_recent()
		if self.type == MatchType.LIVE: return self.matches_live()
		if self.type == MatchType.EXACT: return self.matches_id()


	def matches_recent(self):
		'''
		Recent matches string representation.
		'''
		d = self.data
		return ('-> {}\n'
				'ID: {}, duration: {:2d}:{:02d}\n'
				'{:20} {:3d}{}\n'
				'{:20} {:3d}{}\n').format(d['league_name'],
								          d['match_id'],
								          int(d['duration']/60),
								          d['duration']%60,
								          d['radiant_name'] or kUNKNOWN,
								          d['radiant_score'],
								          ' WON' if d['radiant_win'] else '',
								          d['dire_name'] or kUNKNOWN,
								          d['dire_score'],
								          ' WON' if not d['radiant_win'] else '')


	def matches_live(self):
		'''
		Live matches string representation.
		'''
		d = self.data
		return  '-> {}, Time: {:02d}:{:02d} (avg: {:>4d} MMR) Radiant {:2d} - {:2d} Dire'.format(d['match_id'],
																							    int(d['game_time']/60),
																							    d['game_time']%60,
																							    d['average_mmr'],
																							    d['radiant_score'],
																							    d['dire_score']) +\
				''.join(['\n    {}{} ({})'.format((p['team_tag'] + '.') if p['team_tag'] else '',
				                                  p['name'],
				                                  kHEROES[p['hero_id']]) for p in d['players'] if p.get('is_pro', False)])


	def match_players_str(self, radiant):
		'''
		Players of the match string representation.
		'''
		d = self.data
		if radiant: players = list(filter(lambda a: a['isRadiant'], d['players']))
		else:       players = list(filter(lambda a: not a['isRadiant'], d['players']))
		return '\n'.join(['{:23}   {:>2d} / {:>2d} / {:>2d}  networth: {:>5d}\n  {:20}   LVL {}   GPM {}   XPM {}'
			.format(p.get('personaname', kUNKNOWN), 
                   p['kills'],
                   p['deaths'],
                   p['assists'],
                   p['total_gold'],
		           kHEROES[p['hero_id']],
			       p['level'],
			       p['gold_per_min'],
			       p['xp_per_min']) 
			for p in players
		])


	def matches_id(self):
		'''
		Exact match string representation.
		'''
		d = self.data
		return '\n'.join([
			self.match_players_str(radiant=True),
			'\n{:30}   {}{}\n{:30}   {}{}\n'.format(d['radiant_team_id'] or 'Radiant',
												    d['radiant_score'],
												    '   WON' if self.data['radiant_win'] else '',
												    d['dire_team_id'] or 'Dire',
												    d['dire_score'],
												    '   WON' if not self.data['radiant_win'] else ''),
			self.match_players_str(radiant=False)])
