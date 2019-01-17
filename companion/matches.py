import click
from enum import Enum
from .helpers import *
from . import endpoints as e
from . import heroes as h


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
	if type == MatchType.RECENT: print_matches_recent(data)
	if type == MatchType.LIVE: print_matches_live(data)
	if type == MatchType.EXACT: print_matches_id(data)


def print_matches_recent(data):
	for e in data:
		print('-> {0}'.format(e['league_name']))
		print('ID: {0}, duration: {1:02d}:{2:02d}'.format(e['match_id'], int(e['duration']/60), e['duration']%60))
		print('{0:30} {1:3d}'.format(e['radiant_name'] or 'unknown', e['radiant_score']) + ('   WINNER' if e['radiant_win'] else ''))
		print('{0:30} {1:3d}'.format(e['dire_name'] or 'unknown', e['dire_score']) + ('   WINNER' if not e['radiant_win'] else ''))


def print_matches_live(data):
	data.sort(key=lambda a: a['sort_score'])
	for e in data[:10]:
		print('-> {0} {1:02d}:{2:02d} (avg: {3} MMR)'.format(e['match_id'], int(e['game_time']/60), e['game_time']%60, e['average_mmr']))
		print('Radiant {0:2d} - {1:2d} Dire'.format(e['radiant_score'], e['dire_score']))
		for p in e['players']:
			if p.get('is_pro', False):
				print('{0}.{1} ({2})'.format(p['team_tag'], p['name'], h.heroes[p['hero_id']]))


def print_matches_id(data):
	radiant_players = list(filter(lambda a: a['isRadiant'], data['players']))
	dire_players = list(filter(lambda a: not a['isRadiant'], data['players']))
	print('{0}   {1}{2}'.format('Radiant', data['radiant_score'], '   WINNER' if data['radiant_win'] else ''))
	for p in radiant_players:
		print('{0}   {1}/{2}/{3}   {4}'.format(p['name'] or p['personaname'], p['kills'], p['deaths'], p['assists'], p['gold_spent']))
		print('   {0}   LVL {1}   GPM {2}   XPM {3}'.format(h.heroes[p['hero_id']], p['level'], p['gold_per_min'], p['xp_per_min']))
		print('')
	print('{0}   {1}{2}'.format('Dire', data['dire_score'], '   WINNER' if not data['radiant_win'] else ''))
	for p in dire_players:
		print('{0}   {1}/{2}/{3}   {4}'.format(p['name'] or p['personaname'], p['kills'], p['deaths'], p['assists'], p['gold_spent']))
		print('   {0}   LVL {1}   GPM {2}   XPM {3}'.format(h.heroes[p['hero_id']], p['level'], p['gold_per_min'], p['xp_per_min']))
		print('')


def validate_teams(ctx, param, value):
	try:
		if len(value) > 2:
			raise click.BadParameter('Team max len 2!')
		return value
	except ValueError as e:
		print(e)


def endpoint(id_, live):
	if live:
		return e.live
	else:
		return e.matches + '/' + id_ if id_ else e.pro_matches
