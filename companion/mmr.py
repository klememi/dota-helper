from ascii_graph import Pyasciigraph
from . import helpers as h
from .constants import *


endpoint = '/distributions'


def process_mmr(data, ranks, country):
	if ranks: return print_mmr_rank(data)
	if country: return print_mmr_country(data, country)
	return print_mmr(data)


def print_mmr(data):
	dist = []
	for r in data['mmr']['rows']:
		dist.append((r['bin_name'], r['count']))
	for line in Pyasciigraph().graph('Current Dota 2 players distribution by MMR', dist):
	    print(line)


def print_mmr_rank(data):
	dist = []
	for r in data['ranks']['rows']:
		dist.append((kRANKS[r['bin_name']], r['count']))
	for line in Pyasciigraph().graph('Current Dota 2 players distribution by ranks', dist):
	    print(line)


def print_mmr_country(data, country):
	data = h.filter_substr(['loccountrycode', 'common'], country, data['country_mmr']['rows'])
	if not data:
		return print('Country \'{}\' not found.'.format(country))
	data.sort(key=lambda a: a['common'])
	for c in data:
		print('{:50} -> avg MMR: {:4}, players: {:6}'.format(c['common'], 
												             c['avg'], 
														     c['count']))
