import click
from .helpers import *
from .constants import *
from . import heroes as h
from .match import *


live_endpoint        = '/live'
pro_matches_endpoint = '/proMatches'
matches_endpoint     = '/matches'
team_filter          = ['radiant_name', 'dire_name']
league_filter        = ['league_name']


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
	if not data: return print(kNO_DATA)
	matches = [Match(d, type) for d in data[:10]]
	for m in matches:
		print(m)


def validate_teams(ctx, param, value):
	try:
		if len(value) > 2:
			raise click.BadParameter('You can specify max 2 teams.')
		return value
	except ValueError as e:
		print(e)


def endpoint(id_, live):
	if live:
		return live_endpoint
	else:
		return matches_endpoint + '/' + id_ if id_ else pro_matches_endpoint
