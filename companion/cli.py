from click import command, option, group, version_option, pass_context
import configparser
from .helpers import *
from .match import MatchType
from . import favourite as f
from . import heroes    as h
from . import matches   as m
from . import players   as p
from . import mmr       as r


@group('dotacli')
@version_option(version=1.0, prog_name='Dota 2 Companion')
@option('-c', '--config', 
		default='./dotacli.cfg',
		help='Configuration file path.')
@option('-i', '--id', 'id_',
		default='',
		type=str,
	    help='Your account ID.')
@pass_context
def cli(ctx, config, id_):
	cfg = configparser.ConfigParser()
	cfg.optionxform = str
	cfg.read(config)
	if not 'favourite' in cfg:
		cfg.add_section('favourite')
		cfgfile = open(config, 'w')
		cfg.write(cfgfile)
		cfgfile.close()
	if not 'private' in cfg:
		cfg.add_section('private')
		cfgfile = open(config, 'w')
		cfg.write(cfgfile)
		cfgfile.close()
	if id_:
		cfg.set('private', 'id', id_)
		cfgfile = open(config, 'w')
		cfg.write(cfgfile)
		cfgfile.close()
	ctx.obj['id'] = cfg.get('private', 'id', fallback=id_)
	ctx.obj['favourite'] = cfg['favourite']
	ctx.obj['cfg'] = cfg
	ctx.obj['cfgfile'] = config


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
		mutually_exclusive=['country, team, name, id_, me'])
@option('-c', '--country', 
		type=str,
		help='Filter players by country.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_, me'])
@option('-t', '--team', 
		type=str,
		help='Filter players by team.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_, me'])
@option('-n', '--name', 
		type=str,
		help='Filter players by name.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, id_, me'])
@option('-i', '--id', 'id_',
		type=str,
		help='Player ID.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['favourite, country, team, name, me'])
@option('-m', '--me',
	    is_flag=True,
	    help='Show your personal info.',
	    cls=MutuallyExclusiveOption,
	    mutually_exclusive=['favourite, country, team, name, id_'])
@pass_context
def players(ctx, favourite, country, team, name, id_, me):
	if me:
		if ctx.obj.get('id'): return p.players_id(ctx.obj.get('id'))
		else: return print('You need to provide your account ID.')
	if favourite: return p.players_favourite(ctx.obj['favourite'])
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
@pass_context
def heroes(ctx, name, best, meta, counter):
	if best and not name and ctx.obj.get('id'):
		return p.best_heroes(ctx.obj.get('id'))
	if (best or counter) and not name:
		return print('Please specify hero.')
	try:
		data = get_response_json(h.endpoint(name, best, meta, counter))
	except Exception as err:
		return print(err)
	h.process_heroes(data, name, best, meta, counter, ctx.obj.get('id'))


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


@cli.command(help='Manage favourite players.')
@option('-a', '--add',
		type=str,
		help='Add player to favourites.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['remove'])
@option('-r', '--remove',
		type=str,
		help='Remove player from favourites.',
		cls=MutuallyExclusiveOption,
		mutually_exclusive=['add'])
@pass_context
def favourite(ctx, add, remove):
	if add: return f.favourite_add(add, ctx.obj.get('cfg'), ctx.obj.get('cfgfile'))
	if remove: return f.favourite_remove(remove, ctx.obj.get('cfg'), ctx.obj.get('cfgfile'))
	return print('Please chose either of -a/-r options.')


def main():
	cli(obj={})
