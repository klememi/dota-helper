from . import mmr as r
from . import players as p
from .helpers import filter_substr
from .constants import *


def endpoint(name, best, meta, counter):
	'''
	Defines endpoint to use based on parameters.

	:param name: Name of the hero.
	:param best: Boolean whether to use endpoint for best heroes.
	:param meta: Boolean whether to use endpoint for meta heroes.
	:param meta: Boolean whether to use endpoint for counter heroes.
	:return: Endpoint string.
	'''
	hero_id = list(kHEROES.keys())[list(kHEROES.values()).index(name)] if name in kHEROES.values() else 0
	if best: return '/rankings?hero_id={}'.format(hero_id)
	if meta: return '/heroStats'
	if counter: return '/heroes/{}/matchups'.format(hero_id)
	return '/heroes'


def process_heroes(data, name, best, meta, counter, id_):
	'''
	Processes data based on given parameters and prints data to stdout.

	:param name: Name of the hero.
	:param best: Boolean whether to process data as best heroes.
	:param meta: Boolean whether to process data as meta heroes.
	:param counter: Boolean whether to process data as counter heroes.
	:param id_: Player ID for personalized counter heroes.
	'''
	if best: return print_heroes_best(data)
	if meta: return print_heroes_meta(data)
	if counter: return print_heroes_counter(data, id_)
	return print_heroes_stats(data, name)


def print_heroes_best(data):
	'''
	Prints best heroes data.

	:param data: Data to be printed.
	'''
	if data['hero_id'] == 0: return print(kNO_DATA)
	for x, p in enumerate(data['rankings'][:10]):
		print('{:2d} {:30} ID: {:<10d} ({})'.format(x+1, 
												    p['name'] or p['personaname'] or kUNKNOWN,
												    p['account_id'],
												    kRANKS[p['rank_tier']] if p['rank_tier'] else kUNKNOWN))


def print_heroes_meta(data):
	'''
	Prints meta heroes data.

	:param data: Data to be printed.
	'''
	data.sort(key=lambda a: a['pro_pick'] + a['pro_ban'], reverse=True)
	for h in data[:12]:
		print('{:20}picked: {:<5}banned: {:<5}winrate: {:<5.1f}%'.format(kHEROES[h['hero_id']], 
																		 h['pro_pick'], 
																		 h['pro_ban'], 
																		 100 * h['pro_win'] / h['pro_pick']))


def print_heroes_counter(data, id_):
	'''
	Prints counter heroes data.

	:param data: Data to be printed.
	:param id_: Player ID to be used for personalized counter heroes.
	'''
	if not data: return print(kNO_DATA)
	relevant_heroes = kHEROES.keys()
	if id_:
		try:
			heroes = p.players_heroes(id_)
		except Exception as err:
			return print(err)
		heroes = list(filter(lambda a: a['games'] > 10, heroes))
		relevant_heroes = list(map(lambda a: int(a['hero_id']), heroes))
	relevant_data = list(filter(lambda a: a['games_played'] > 10 and a['hero_id'] in relevant_heroes, data))
	if not relevant_data:
		relevant_heroes = kHEROES.keys()
		relevant_data = list(filter(lambda a: a['games_played'] > 20 and a['hero_id'] in relevant_heroes, data))
	relevant_data.sort(key=lambda a: a['wins'] / a['games_played'])
	for h in relevant_data[:12]:
		print('{:20}winrate: {:<5.1f}%'.format(kHEROES[h['hero_id']], 
									           100 * h['wins'] / h['games_played']))


def print_heroes_stats(data, name):
	'''
	Prints heroes data.

	:param data: Data to be printed.
	:param name: Hero name.
	'''
	if name:
		data = filter_substr(['localized_name'], name, data)
	for h in data:
		print('{:20}{:6} {:12}   roles: {}'.format(h['localized_name'], 
												   h['attack_type'], 
												   primary(h['primary_attr']), 
												   ', '.join(h['roles'])))


def primary(attr):
	'''
	Returns attribute name based on shortcut.

	:param attr: Attribute shortcut.
	:return: Attribute name.
	'''
	return 'Agility' if attr == 'agi' else 'Strength' if attr == 'str' else 'Intelligence'
