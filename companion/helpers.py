from click import Option, UsageError
import requests
from functools import reduce


url = 'https://api.opendota.com/api'


def get_response(endpoint):
	response = requests.get(url + endpoint)
	if response.status_code != requests.codes.ok:
		response.raise_for_status()
	return response


def filter_eq(keys, value, array):
	return filter_by_multiple_keys(lambda a: [a[key] == value for key in keys], array)


def filter_substr(keys, value, array):
	return filter_by_multiple_keys(lambda a: [str(a[key]).lower().find(value.lower()) >= 0 for key in keys], array)


def filter_by_multiple_keys(keys, array):
	return list(filter(lambda a: reduce(lambda b, c: b or c, keys(a)), array))


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
