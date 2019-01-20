import click
from enum import Enum
from .helpers import *
from .constants import *
from . import heroes as h


live_endpoint        = '/live'
pro_matches_endpoint = '/proMatches'
matches_endpoint     = '/matches'
team_filter          = ['radiant_name', 'dire_name']
league_filter        = ['league_name']


class MatchType(Enum):
	RECENT = 1
	LIVE   = 2
	EXACT  = 3


def process_matches(type, data, team=None, league=None):
	if type == MatchType.EXACT:
		return print(Match(data, type))
	if type == MatchType.RECENT:
		if team:
			data = filter_substr(team_filter, team[0], data)
			if len(team) == 2:
				data = filter_substr(team_filter, team[1], data)
		if league:
			data = filter_substr(league_filter, league, data)
		data.sort(key=lambda a: a['start_time'], reverse=True)
	if type == MatchType.LIVE:
		data.sort(key=lambda a: a['sort_score'], reverse=True)
	matches = [Match(d, type) for d in data[:10]]
	for m in matches:
		print(m)


class Match:
	def __init__(self, data, type):
		self.type = type
		self.data = data


	def __str__(self):
		if not self.data: return kNO_DATA
		if self.type == MatchType.RECENT: return self.matches_recent()
		if self.type == MatchType.LIVE: return self.matches_live()
		if self.type == MatchType.EXACT: return self.matches_id()


	def matches_recent(self):
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
		d = self.data
		if radiant: players = list(filter(lambda a: a['isRadiant'], d['players']))
		else:       players = list(filter(lambda a: not a['isRadiant'], d['players']))
		return '\n'.join(['{:23}   {:>2d} / {:>2d} / {:>2d}  networth: {:>5d}\n  {:20}   LVL {}   GPM {}   XPM {}'
			.format(p['name'] or p['personaname'] or kUNKNOWN, 
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
		d = self.data
		return '\n'.join([
			self.match_players_str(radiant=True),
			'\n{:30}   {}{}\n{:30}   {}{}\n'.format(d['radiant_team']['name'] or 'Radiant',
												    d['radiant_score'],
												    '   WON' if self.data['radiant_win'] else '',
												    d['dire_team']['name'] or 'Dire',
												    d['dire_score'],
												    '   WON' if not self.data['radiant_win'] else ''),
			self.match_players_str(radiant=False)])


def validate_teams(ctx, param, value):
	try:
		if len(value) > 2:
			raise click.BadParameter('Team max len 2!')
		return value
	except ValueError as e:
		print(e)


def endpoint(id_, live):
	if live:
		return live_endpoint
	else:
		return matches_endpoint + '/' + id_ if id_ else pro_matches_endpoint
