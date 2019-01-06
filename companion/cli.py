import click
import requests
from functools import reduce
from tabulate import tabulate
from time import strftime


url = 'https://api.opendota.com/api'


def filter_eq(keys, value, array):
	return list(filter(lambda a: reduce(lambda b, c: b or c, [a[key] == value for key in keys]), array))


def filter_str(keys, value, array):
	return list(filter(lambda a: reduce(lambda b, c: b or c, [str(a[key]).lower().find(value.lower()) >= 0 for key in keys]), array))


def choose(keys, array):
	return list(map(lambda x: [x[key] for key in keys], array))


@click.group('dotacli')
@click.version_option(version=1.0, prog_name='Dota 2 Companion')
def cli():
	print('cli')


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
@click.option('--pro/--public')
@click.option('--team1', type=str)
@click.option('--team2', type=str)
@click.option('--league', type=str)
def matches(pro, team1, team2, league):
	endpoint = '/proMatches' if pro else '/matches'
	r = requests.get(url + endpoint)
	result = r.json()
	if team1:
		result = filter_str(['radiant_name', 'dire_name'], team1, result)
	if team2:
		result = filter_str(['radiant_name', 'dire_name'], team2, result)
	result = choose(['radiant_name', 'dire_name', 'league_name'], result)
	print(tabulate(result, headers=['radiant', 'dire', 'league']))


@cli.command()
@click.option('--pro')
def heroes():
	pass


@cli.command()
@click.option('--pro')
def mmr():
	pass


def main():
	cli()