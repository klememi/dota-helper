import click
import requests


url = 'https://api.opendota.com/api'


def filter_by(key, value, array):
	return list(filter(lambda x: x[key] == value, array))


@click.group('dotacli')
@click.version_option(version=1.0, prog_name='Dota 2 Companion')
def cli():
	print('cli')


@cli.command()
@click.option('-p', '--pro', is_flag=True)
@click.option('-c', '--country', type=str)
@click.option('-t', '--team', type=str)
# @click.option('-r', '--role', type=click.IntRange(min=1, max=5, clamp=False))
@click.option('-n', '--name', type=str)
def players(pro, country, team, role, name):
	endpoint = '/proPlayers' if pro else '/players'
	r = requests.get(url + endpoint)
	result = r.json()
	if team:
		result = list(filter(lambda x: x['team_name'] == team || x['team_tag'] == team, result))
	if country:
		result = filter_by('loccountrycode', country, result)
	if name:
		result = filter_by('name', name, result)
	print(result)


@cli.command()
@click.option('--pro')
def matches():
	pass


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