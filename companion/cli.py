from click import command, option, group, version_option
from .helpers import *
from . import heroes  as h
from . import matches as m
from . import players as p
from . import mmr     as r


@group('dotacli')
@version_option(version=1.0, prog_name='Dota 2 Companion')
def cli():
	pass


@cli.command(help='')
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
		data = get_response_json(m.endpoint(id_, live))
	except Exception as err:
		return print(err)
	if id_: type = m.MatchType.EXACT
	elif live: type = m.MatchType.LIVE
	else: type = m.MatchType.RECENT
	return m.process_matches(type, data, team, league)


@cli.command(help='')
@option('-f', '--favourite', 
		is_flag=True,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['country, team, name, id_'])
@option('-c', '--country', 
		type=str,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_'])
@option('-t', '--team', 
		type=str,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_'])
@option('-n', '--name', 
		type=str,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_'])
@option('-i', '--id', 'id_',
		type=str,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, country, team, name'])
def players(favourite, country, team, name, id_):
	if favourite: return p.players_favourite()
	if id_:       return p.players_id(id_)
	try:
		data = get_response_json(p.pro_players_endpoint)
	except Exception as err:
		return print(err)
	p.process_players(data, country, team, name)


@cli.command(help='')
@option('-n', '--name', 
		type=str,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['meta'])
@option('-b', '--best', 
		is_flag=True,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['meta', 'counter'])
@option('-m', '--meta', 
		is_flag=True,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['name', 'best', 'counter'])
@option('-c', '--counter', 
		is_flag=True,
		help='',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['best', 'meta'])
def heroes(name, best, meta, counter):
	if (best or counter) and not name:
		return print('Please specify hero.')
	try:
		data = get_response_json(h.endpoint(name, best, meta, counter))
	except Exception as err:
		return print(err)
	h.process_heroes(data, name, best, meta, counter)


@cli.command(help='')
@option('-r', '--ranks', 
		is_flag=True,
	    help='Ranks',
	    cls=MutuallyExclusiveOption,
	    mutually_exclusive=['country'])
@option('-c', '--country',
		type=str,
	    help='Country',
	    cls=MutuallyExclusiveOption,
	    mutually_exclusive=['ranks'])
def mmr(ranks, country):
	try:
		data = get_response_json(r.endpoint)
	except Exception as err:
		return print(err)
	r.process_mmr(data, ranks, country)


def main():
	cli()
