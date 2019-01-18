from . import mmr as r
from .helpers import filter_substr


heroes = {
	0: '<picking>',
	1: 'Anti-Mage',
	2: 'Axe',
	3: 'Bane',
	4: 'Bloodseeker',
	5: 'Crystal Maiden',
	6: 'Drow Ranger',
	7: 'Earthshaker',
	8: 'Juggernaut',
	9: 'Mirana',
	10: 'Morphling',
	11: 'Shadow Fiend',
	12: 'Phantom Lancer',
	13: 'Puck',
	14: 'Pudge',
	15: 'Razor',
	16: 'Sand King',
	17: 'Storm Spirit',
	18: 'Sven',
	19: 'Tiny',
	20: 'Vengeful Spirit',
	21: 'Windranger',
	22: 'Zeus',
	23: 'Kunkka',
	25: 'Lina',
	26: 'Lion',
	27: 'Shadow Shaman',
	28: 'Slardar',
	29: 'Tidehunter',
	30: 'Witch Doctor',
	31: 'Lich',
	32: 'Riki',
	33: 'Enigma',
	34: 'Tinker',
	35: 'Sniper',
	36: 'Necrophos',
	37: 'Warlock',
	38: 'Beastmaster',
	39: 'Queen of Pain',
	40: 'Venomancer',
	41: 'Faceless Void',
	42: 'Wraith King',
	43: 'Death Prophet',
	44: 'Phantom Assassin',
	45: 'Pugna',
	46: 'Templar Assassin',
	47: 'Viper',
	48: 'Luna',
	49: 'Dragon Knight',
	50: 'Dazzle',
	51: 'Clockwerk',
	52: 'Leshrac',
	53: "Nature's Prophet",
	54: 'Lifestealer',
	55: 'Dark Seer',
	56: 'Clinkz',
	57: 'Omniknight',
	58: 'Enchantress',
	59: 'Huskar',
	60: 'Night Stalker',
	61: 'Broodmother',
	62: 'Bounty Hunter',
	63: 'Weaver',
	64: 'Jakiro',
	65: 'Batrider',
	66: 'Chen',
	67: 'Spectre',
	68: 'Ancient Apparition',
	69: 'Doom',
	70: 'Ursa',
	71: 'Spirit Breaker',
	72: 'Gyrocopter',
	73: 'Alchemist',
	74: 'Invoker',
	75: 'Silencer',
	76: 'Outworld Devourer',
	77: 'Lycan',
	78: 'Brewmaster',
	79: 'Shadow Demon',
	80: 'Lone Druid',
	81: 'Chaos Knight',
	82: 'Meepo',
	83: 'Treant Protector',
	84: 'Ogre Magi',
	85: 'Undying',
	86: 'Rubick',
	87: 'Disruptor',
	88: 'Nyx Assassin',
	89: 'Naga Siren',
	90: 'Keeper of the Light',
	91: 'Io',
	92: 'Visage',
	93: 'Slark',
	94: 'Medusa',
	95: 'Troll Warlord',
	96: 'Centaur Warrunner',
	97: 'Magnus',
	98: 'Timbersaw',
	99: 'Bristleback',
	100: 'Tusk',
	101: 'Skywrath Mage',
	102: 'Abaddon',
	103: 'Elder Titan',
	104: 'Legion Commander',
	105: 'Techies',
	106: 'Ember Spirit',
	107: 'Earth Spirit',
	108: 'Underlord',
	109: 'Terrorblade',
	110: 'Phoenix',
	111: 'Oracle',
	112: 'Winter Wyvern',
	113: 'Arc Warden',
	114: 'Monkey King',
	119: 'Dark Willow',
	120: 'Pangolier',
	121: 'Grimstroke'
}


def endpoint(name, best, meta, counter):
	hero_id = list(heroes.keys())[list(heroes.values()).index(name)] if name in heroes.values() else 0
	if best: return '/rankings?hero_id={}'.format(hero_id)
	if meta: return '/heroStats'
	if counter: return '/heroes/{}/matchups'.format(hero_id)
	return '/heroes'


def process_heroes(data, name, best, meta, counter):
	if best: return print_heroes_best(data)
	if meta: return print_heroes_meta(data)
	if counter: return print_heroes_counter(data)
	return print_heroes_stats(data, name)


def print_heroes_best(data):
	for x, p in enumerate(data['rankings'][:10]):
		print('{:2d} {:20} ID: {:<10d} ({})'.format(x+1, 
												   p['name'] or p['personaname'],
												   p['account_id'],
												   r.ranks[p['rank_tier']])
		)


def print_heroes_meta(data):
	data.sort(key=lambda a: a['pro_pick'] + a['pro_ban'], reverse=True)
	for h in data[:12]:
		print('{:20}picked: {:<5}banned: {:<5}winrate: {:<5.1f}%'.format(heroes[h['hero_id']], 
																		 h['pro_pick'], 
																		 h['pro_ban'], 
																		 100 * h['pro_win'] / h['pro_pick']))


def print_heroes_counter(data):
	data = list(filter(lambda a: a['games_played'] > 30, data))
	data.sort(key=lambda a: a['wins'] / a['games_played'])
	for h in data[:12]:
		print('{:20}winrate: {:<5.1f}%'.format(heroes[h['hero_id']], 
									           100 * h['wins'] / h['games_played']))


def print_heroes_stats(data, name):
	data = filter_substr(['localized_name'], name, data)
	for h in data:
		print('{:20}{:6} {:12}   roles: {}'.format(h['localized_name'], 
												   h['attack_type'], 
												   primary(h['primary_attr']), 
												   ', '.join(h['roles'])))


def primary(attr):
	return 'Agility' if attr == 'agi' else 'Strength' if attr == 'str' else 'Intelligence'
