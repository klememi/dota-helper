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
