from click import command, option, group, version_option
from . import heroes as h
from . import matches as m
from . import players as p
from . import mmr as r
from .helpers import *


@group('dotacli')
@version_option(version=1.0, prog_name='Dota 2 Companion')
def cli():
	pass


@cli.command()
@option('-t', '--team', 
			  type=str,
			  cls=MutuallyExclusiveOption,
			  multiple=True,
			  callback=m.validate_teams,
			  help='Team filter',
			  mutually_exclusive=['id_', 'live'])
@option('-g', '--league', 
			  type=str, 
			  cls=MutuallyExclusiveOption,
			  help='League filter',
			  mutually_exclusive=['id_', 'live'])
@option('-i', '--id', 'id_', 
			  type=str, 
			  cls=MutuallyExclusiveOption,
			  help='match ID',
			  mutually_exclusive=['team', 'league', 'live'])
@option('-l', '--live', 
			  is_flag=True, 
			  cls=MutuallyExclusiveOption,
			  help='Live filter',
			  mutually_exclusive=['team', 'league', 'id_'])
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
@option('-p', '--pro', is_flag=True)
@option('-c', '--country', type=str)
@option('-t', '--team', type=str)
@option('-n', '--name', type=str)
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
@option('-n', '--name', type=str)
@option('-b', '--best', is_flag=True)
@option('-m', '--meta', is_flag=True)
@option('-c', '--counter', is_flag=True)
def heroes(name, best, meta, counter):
	try:
		data = get_response(h.endpoint(name, best, meta, counter)).json()
	except Exception as err:
		return print(err)
	h.process_heroes(data, name, best, meta, counter)


@cli.command()
@option('-r', '--ranks', 
		is_flag=True,
		cls=MutuallyExclusiveOption,
	    help='Ranks',
	    mutually_exclusive=['country'])
@option('-c', '--country',
		type=str,
		cls=MutuallyExclusiveOption,
	    help='Country',
	    mutually_exclusive=['ranks'])
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
