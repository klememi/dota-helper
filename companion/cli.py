from click import command, option, group, version_option
from .helpers import *
from .match import MatchType
from . import heroes  as h
from . import matches as m
from . import players as p
from . import mmr     as r


@group('dotacli')
@version_option(version=1.0, prog_name='Dota 2 Companion')
def cli():
	pass


@cli.command(help='Show matches info.')
@option('-t', '--team', 
			  type=str,
			  cls=MutuallyExclusiveOption,
			  multiple=True,
			  callback=m.validate_teams,
			  help='Filter matches by team.',
			  mutually_exclusive=['id_', 'live'])
@option('-g', '--league', 
			  type=str, 
			  cls=MutuallyExclusiveOption,
			  help='Filter matches by league.',
			  mutually_exclusive=['id_', 'live'])
@option('-i', '--id', 'id_', 
			  type=str, 
			  cls=MutuallyExclusiveOption,
			  help='Match ID.',
			  mutually_exclusive=['team', 'league', 'live'])
@option('-l', '--live', 
			  is_flag=True, 
			  cls=MutuallyExclusiveOption,
			  help='Show live matches.',
			  mutually_exclusive=['team', 'league', 'id_'])
def matches(team, league, id_, live):
	try:
		data = get_response_json(m.endpoint(id_, live))
	except Exception as err:
		return print(err)
	if id_: type = MatchType.EXACT
	elif live: type = MatchType.LIVE
	else: type = MatchType.RECENT
	return m.process_matches(type, data, team, league)


@cli.command(help='Show players info.')
@option('-f', '--favourite', 
		is_flag=True,
		help='Favourite players.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['country, team, name, id_'])
@option('-c', '--country', 
		type=str,
		help='Filter players by country.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_'])
@option('-t', '--team', 
		type=str,
		help='Filter players by team.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_'])
@option('-n', '--name', 
		type=str,
		help='Filter players by name.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_'])
@option('-i', '--id', 'id_',
		type=str,
		help='Player ID.',
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


@cli.command(help='Show heroes info.')
@option('-n', '--name', 
		type=str,
		help='Hero name.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['meta'])
@option('-b', '--best', 
		is_flag=True,
		help='Show best players by hero.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['meta', 'counter'])
@option('-m', '--meta', 
		is_flag=True,
		help='Show heroes in current meta.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['name', 'best', 'counter'])
@option('-c', '--counter', 
		is_flag=True,
		help='Show hero\'s counters',
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


@cli.command(help='Show MMR info.')
@option('-r', '--ranks', 
		is_flag=True,
	    help='Show distribution by ranks.',
	    cls=MutuallyExclusiveOption,
	    mutually_exclusive=['country'])
@option('-c', '--country',
		type=str,
	    help='Show country average MMR.',
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
