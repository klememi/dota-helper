from functools import reduce


def filter_eq(keys, value, array):
	return filter_by_multiple_keys(lambda a: [a[key] == value for key in keys], array)


def filter_substr(keys, value, array):
	return filter_by_multiple_keys(lambda a: [str(a[key]).lower().find(value.lower()) >= 0 for key in keys], array)


def filter_by_multiple_keys(keys, array):
	return list(filter(lambda a: reduce(lambda b, c: b or c, keys(a)), array))


def choose(keys, array):
	return [{key: entry[key] for key in keys} for entry in array]
	# return list(map(lambda x: [x[key] for key in keys], array))
