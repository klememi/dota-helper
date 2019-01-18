import click
from enum import Enum
from .helpers import *
from . import heroes as h


live_endpoint = '/live'
pro_matches_endpoint = '/proMatches'
matches_endpoint = '/matches'
team_filter = ['radiant_name', 'dire_name']
league_filter = ['league_name']


class MatchType(Enum):
	RECENT = 1
	LIVE = 2
	EXACT = 3


def process_matches(type, data, team=None, league=None):
	if type == MatchType.RECENT:
		if team:
			data = filter_substr(team_filter, team[0], data)
			if len(team) == 2:
				data = filter_substr(team_filter, team[1], data)
		if league:
			data = filter_substr(league_filter, league, data)
	print_matches(type, data)


def print_matches(type, data):
	if not data: return print('Data matching your criteria not found.')
	if type == MatchType.RECENT: return print_matches_recent(data)
	if type == MatchType.LIVE: return print_matches_live(data)
	if type == MatchType.EXACT: return print_matches_id(data)


def print_matches_recent(data):
	data.sort(key=lambda a: a['start_time'])
	for e in data[:20]:
		print('-> {}'.format(e['league_name']))
		print('ID: {}, duration: {:2d}:{:02d}'.format(e['match_id'], 
													  int(e['duration']/60),
													  e['duration']%60))
		print('{:20} {:3d}{}'.format(e['radiant_name'] or 'unknown', e['radiant_score'],
									 '  WON' if e['radiant_win'] else ''))
		print('{:20} {:3d}{}'.format(e['dire_name'] or 'unknown', e['dire_score'],
									 '  WON' if not e['radiant_win'] else ''))


def print_matches_live(data):
	data.sort(key=lambda a: a['sort_score'])
	for e in data[:20]:
		print('-> {}, Game time: {:02d}:{:02d} (avg: {} MMR) Radiant {:2d} - {:2d} Dire'.format(e['match_id'], 
																								int(e['game_time']/60), 
																								e['game_time']%60, 
																								e['average_mmr'], 
																								e['radiant_score'], 
																								e['dire_score']))
		for p in e['players']:
			if p.get('is_pro', False):
				print('     {}{} ({})'.format((p['team_tag'] + '.') if p['team_tag'] else '', 
											  p['name'], 
											  h.heroes[p['hero_id']]))


def print_matches_id(data):
	radiant_players = list(filter(lambda a: a['isRadiant'], data['players']))
	dire_players = list(filter(lambda a: not a['isRadiant'], data['players']))
	for p in radiant_players:
		print('{:23}   {:>2d} / {:>2d} / {:>2d}  networth: {:>5d}'.format(p['name'] or p['personaname'], 
										                                  p['kills'], 
										                                  p['deaths'], 
										                                  p['assists'], 
										                                  p['total_gold']))
		print('   {:20}   LVL {}   GPM {}   XPM {}'.format(h.heroes[p['hero_id']], 
														   p['level'], 
														   p['gold_per_min'], 
														   p['xp_per_min']))
	print('')
	print('{:30}   {}{}'.format(data['radiant_team']['name'] or 'Radiant', 
							    data['radiant_score'], 
							    '   WON' if data['radiant_win'] else ''))
	print('{:30}   {}{}'.format(data['dire_team']['name'] or 'Dire', 
							    data['dire_score'], 
							    '   WON' if not data['radiant_win'] else ''))
	print('')
	for p in dire_players:
		print('{:23}   {:>2d} / {:>2d} / {:>2d}  networth: {:>5d}'.format(p['name'] or p['personaname'], 
									                                      p['kills'], 
									                                      p['deaths'], 
									                                      p['assists'], 
									                                      p['total_gold']))
		print('   {:20}   LVL {}   GPM {}   XPM {}'.format(h.heroes[p['hero_id']], 
														   p['level'], 
														   p['gold_per_min'], 
														   p['xp_per_min']))


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
