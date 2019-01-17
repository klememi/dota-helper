import click
from . import matches as m
from . import players as p
from . import mmr as r
from .helpers import *


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
		data = get_response(m.endpoint(id_, live)).json()
	except Exception as err:
		return print(err)
	if id_: type = m.MatchType.EXACT
	elif live: type = m.MatchType.LIVE
	else: type = m.MatchType.RECENT
	return m.process_matches(type, data, team, league)


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
@click.option('-r', '--ranks', is_flag=True)
@click.option('-c', '--country', type=str)
def mmr(ranks, country):
	try:
		data = get_response(r.endpoint).json()
	except Exception as err:
		return print(err)
	r.process_mmr(data, ranks, country)


@cli.command()
def teams():
	pass


def main():
	cli()
