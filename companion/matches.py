import click
from . import endpoints as e


def validate_teams(ctx, param, value):
	try:
		if len(value) > 2:
			raise click.BadParameter('Team max len 2!')
		return value
	except ValueError as e:
		print(e)


def endpoint(pro, live):
	if live:
		return e.live
	else:
		return e.pro_matches if pro else e.matches


team_filter = ['radiant_name', 'dire_name']
league_filter = ['league_name']
id_filter = ['match_id']
table_headers = ['radiant', 'dire', 'league']
chosen_cols = ['radiant_name', 'dire_name', 'league_name']