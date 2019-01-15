import click
import requests
import time
from . import matches as m
from . import players as p
from . import errors as e
from .helpers import *
from tabulate import tabulate
from time import strftime


url = 'https://api.opendota.com/api'


@click.group('dotacli')
@click.version_option(version=1.0, prog_name='Dota 2 Companion')
def cli():
	pass


@cli.command()
@click.option('-t', '--team', type=str, multiple=True, callback=m.validate_teams)
@click.option('-g', '--league', type=str)
@click.option('-i', '--id', 'id_', type=str)
@click.option('-l', '--live', is_flag=True)
def matches(team, league, id_, live):
	try:
		response = requests.get(url + m.endpoint(id_, live))
		if response.status_code != 200:
			raise e.BadRequestError()
	except e.BadRequestError as err:
		print('BadRequestError')
		return
	data = response.json()
	if id_:
		return exact_match(data)
	if team:
		data = filter_substr(m.team_filter, team[0], data)
		if len(team) == 2:
			data = filter_substr(m.team_filter, team[1], data)
	if league:
		data = filter_substr(m.league_filter, league, data)
	print_matches(data)


def print_matches(data):
	for e in data:
		print('-> {0}'.format(e['league_name']))
		print('ID: {0}, duration: {1:02d}:{2:02d}'.format(e['match_id'], int(e['duration']/60), e['duration']%60))
		print('{0:30} {1:3d}'.format(e['radiant_name'] or 'unknown', e['radiant_score']) + ('   WINNER' if e['radiant_win'] else ''))
		print('{0:30} {1:3d}'.format(e['dire_name'] or 'unknown', e['dire_score']) + ('   WINNER' if not e['radiant_win'] else ''))


def exact_match(data):
	pass


@cli.command()
@click.option('-p', '--pro', is_flag=True)
@click.option('-c', '--country', type=str)
@click.option('-t', '--team', type=str)
@click.option('-n', '--name', type=str)
def players(pro, country, team, name):
	endpoint = '/proPlayers' if pro else '/players'
	r = requests.get(url + endpoint)
	result = r.json()
	if team:
		result = filter_str(['team_name', 'team_tag'], team, result)
	if country:
		result = filter_str(['loccountrycode', 'country_code'], country, result)
	if name:
		result = filter_str(['personaname', 'name'], name, result)
	result = list(map(lambda x: [x['name'], x['team_name']], result))
	print(tabulate(result, headers=['name', 'team']))


@cli.command()
def heroes():
	pass


@cli.command()
def mmr():
	pass


@cli.command()
def teams():
	pass


def main():
	cli()
