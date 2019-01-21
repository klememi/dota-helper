import configparser
from . import players as p


def favourite_add(add, cfg, file):
	'''
	Adds player ID to the favourites in the config file.

	:param add: Player ID to be added.
	:param cfg: ConfigParser instance with loaded actual config file.
	:param file: Path to the config file.
	'''
	if add in cfg['favourite'] and cfg['favourite'][add] == 'yes':
		return print('This player is already in your favourites.')
	else:
		if p.player_id_is_ok(add):
			cfg.set('favourite', add, 'yes')
			cfgfile = open(file, 'w')
			cfg.write(cfgfile)
			cfgfile.close()
			print('Player {} added to your favourites.'.format(add))
		else:
			print('This ID is not valid.')


def favourite_remove(remove, cfg, file):
	'''
	Removes player ID from the favourites in the config file.

	:param add: Player ID to be removed.
	:param cfg: ConfigParser instance with loaded actual config file.
	:param file: Path to the config file.
	'''
	if remove not in cfg['favourite'] or cfg['favourite'][remove] == 'yes':
		return print('This player is not in your favourites.')
	else:
		cfg.set('favourite', remove, 'no')
		cfgfile = open(file, 'w')
		cfg.write(cfgfile)
		cfgfile.close()
		print('Player {} removed from your favourites.'.format(remove))