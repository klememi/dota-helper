import requests
from click import Option, UsageError
from functools import reduce


url = 'https://api.opendota.com/api'
session = requests.Session()


def get_response_json(endpoint, session=session):
	'''
	Sends request to the API.

	:param endpoint: Endpoint to be used for the request.
	:param session: Session to be used for HTTP comm.
	:return: JSON object with response.
	'''
	with session as s:
		response = s.get(url + endpoint)
		if response.status_code != requests.codes.ok:
			response.raise_for_status()
		return response.json()


def filter_eq(keys, value, array):
	'''
	Filters array of dicts by equality of given value with one of the define keys.

	:param keys: Keys used for the comparison.
	:param value: Value used for the comparison.
	:param array: Array of dicts to be filtered.
	:return: Filtered array of dicts.
	'''
	return filter_by_multiple_keys(lambda a: [a[key] == value for key in keys], array)


def filter_substr(keys, value, array):
	'''
	Filters array of dicts by finding substring under one of the given keys.

	:param keys: Keys used for the comparison.
	:param value: Value used for the comparison.
	:param array: Array of dicts to be filtered.
	:return: Filtered array of dicts.
	'''
	return filter_by_multiple_keys(lambda a: [str(a[key]).lower().find(value.lower()) >= 0 for key in keys], array)


def filter_by_multiple_keys(f, array):
	'''
	Base function used for the filtering.

	:param f: Function used for the filtering.
	:param array: Array of dicts to be filtered.
	:return: Filtered array.
	'''
	return list(filter(lambda a: reduce(lambda b, c: b or c, f(a)), array))


class MutuallyExclusiveOption(Option):
	def __init__(self, *args, **kwargs):
		self.mutually_exclusive = set(kwargs.pop('mutually_exclusive', []))
		help = kwargs.get('help', '')
		if self.mutually_exclusive:
			ex_str = ', '.join(self.mutually_exclusive)
			kwargs['help'] = help + (
				' NOTE: This argument is mutually exclusive with '
				' arguments: [' + ex_str + '].'
			)
		super(MutuallyExclusiveOption, self).__init__(*args, **kwargs)


	def handle_parse_result(self, ctx, opts, args):
		if self.mutually_exclusive.intersection(opts) and self.name in opts:
			raise UsageError(
				"Illegal usage: `{}` is mutually exclusive with "
				"arguments `{}`.".format(
					self.name,
					', '.join(self.mutually_exclusive)
				)
			)

		return super(MutuallyExclusiveOption, self).handle_parse_result(ctx, opts, args)
