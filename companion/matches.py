import click
from . import endpoints as e


def validate_teams(ctx, param, value):
	try:
		if len(value) > 2:
			raise click.BadParameter('Team max len 2!')
		return value
	except ValueError as e:
		print(e)


def endpoint(id_, live):
	if live:
		return e.live
	else:
		return e.matches + '/' + id_ if id_ else e.pro_matches


team_filter = ['radiant_name', 'dire_name']
league_filter = ['league_name']
id_filter = ['match_id']
table_headers = ['radiant', 'dire', 'league']
chosen_cols = ['radiant_name', 'dire_name', 'league_name', 'match_id', 'duration', 'radiant_win', 'radiant_score', 'dire_score']