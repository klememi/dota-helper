import click
import requests
from . import matches as m
from . import players as p
from .helpers import *
from tabulate import tabulate
from time import strftime


url = 'https://api.opendota.com/api'


@click.group('dotacli')
@click.version_option(version=1.0, prog_name='Dota 2 Companion')
def cli():
	pass


@cli.command()
@click.option('--pro/--public')
@click.option('-t', '--team', type=str, multiple=True, callback=m.validate_teams)
@click.option('-g', '--league', type=str)
@click.option('-i', '--id', 'id_', type=str)
@click.option('-l', '--live', is_flag=True)
def matches(pro, team, league, id_, live):	
	if id_:
		return exact_match(id_)
	response = requests.get(url + m.endpoint(pro, live))
	result = response.json()
	if team:
		result = filter_substr(m.league_filter, team[0], result)
		if len(team) == 2:
			result = filter_substr(m.league_filter, team[1], result)
	if league:
		result = filter_substr(m.league_filter, league, result)
	if id_:
		result = filter_substr(m.id_filter, id_, result)
	result = choose(m.chosen_cols, result)
	print(tabulate(result, headers=m.table_headers))


def exact_match(id_):



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
