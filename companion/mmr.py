from ascii_graph import Pyasciigraph
from . import helpers as h


endpoint = '/distributions'
ranks = {
	11: 'Herald I',
	12: 'Herald II',
	13: 'Herald III',
	14: 'Herald IV',
	15: 'Herald V',
	21: 'Guardian I',
	22: 'Guardian II',
	23: 'Guardian III',
	24: 'Guardian IV',
	25: 'Guardian V',
	31: 'Crusader I',
	32: 'Crusader II',
	33: 'Crusader III',
	34: 'Crusader IV',
	35: 'Crusader V',
	41: 'Archon I',
	42: 'Archon II',
	43: 'Archon III',
	44: 'Archon IV',
	45: 'Archon V',
	51: 'Legend I',
	52: 'Legend II',
	53: 'Legend III',
	54: 'Legend IV',
	55: 'Legend V',
	61: 'Ancient I',
	62: 'Ancient II',
	63: 'Ancient III',
	64: 'Ancient IV',
	65: 'Ancient V',
	71: 'Divine I',
	72: 'Divine II',
	73: 'Divine III',
	74: 'Divine IV',
	75: 'Divine V',
	80: 'Immortals'
}


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
		dist.append((ranks[r['bin_name']], r['count']))
	for line in Pyasciigraph().graph('Current Dota 2 players distribution by ranks', dist):
	    print(line)


def print_mmr_country(data, country):
	data = h.filter_substr(['loccountrycode', 'common'], country, data['country_mmr']['rows'])
	if not data:
		return print('Country \'{}\' not found.'.format(country))
	for c in data:
		print('{} -> average MMR: {}, number of players: {}'.format(c['common'], c['avg'], c['count']))
