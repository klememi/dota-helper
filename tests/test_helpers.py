import pytest
import betamax
from companion import helpers as h


with betamax.Betamax.configure() as config:
	config.cassette_library_dir = 'tests/fixtures/cassettes'


def test_request_ok(betamax_session):
	result = h.get_response_json('/distributions', betamax_session)
	assert(result is not None)


def test_request_exception(betamax_session):
	with pytest.raises(Exception):
		h.get_response_json('/not_exists', betamax_session)


@pytest.mark.parametrize(
	['keys', 'value', 'res'],
	[(['a', 'b'], 1, [{'a': 1, 'b': 1}, {'a': 1, 'b': 2}, {'a': 2, 'b': 1}]),
	 (['a', 'b'], 2, [{'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 2, 'b': 2}]),
	 (['b'], 2, [{'a': 1, 'b': 2}, {'a': 2, 'b': 2}]),
	 (['a'], 2, [{'a': 2, 'b': 1}, {'a': 2, 'b': 2}])]
)
def test_filter_eq_ok(keys, value, res):
	r = h.filter_eq(keys, value, [{'a': 1, 'b': 1}, {'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 2, 'b': 2}])
	assert(res == r)


@pytest.mark.parametrize(
	['keys', 'value'],
	[(['a', 'b'], 0),
	 (['a', 'b'], 3),
	 (['b'], 3),
	 (['a'], 3)]
)
def test_filter_eq_empty(keys, value):
	r = h.filter_eq(keys, value, [{'a': 1, 'b': 1}, {'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 2, 'b': 2}])
	assert(not r)


@pytest.mark.parametrize(
	['keys', 'value', 'res'],
	[(['a', 'b'], 'ab', [{'a': 'abcd', 'b': 'cdef'}, {'a': 'abd', 'b': 'cdf'}]),
	 (['a', 'b'], 'cd', [{'a': 'abcd', 'b': 'cdef'}, {'a': 'abd', 'b': 'cdf'}, {'a': 'cd', 'b': 'ef'}]),
	 (['a'], 'ac', [{'a': 'acc', 'b': 'bdd'}]),
	 (['b'], 'df', [{'a': 'abd', 'b': 'cdf'}])]
)
def test_filter_substr_ok(keys, value, res):
	r = h.filter_substr(keys, value, [{'a': 'abcd', 'b': 'cdef'}, {'a': 'acc', 'b': 'bdd'}, {'a': 'abd', 'b': 'cdf'}, {'a': 'cd', 'b': 'ef'}])
	assert(r == res)


@pytest.mark.parametrize(
	['keys', 'value'],
	[(['a', 'b'], 'ff'),
	 (['a', 'b'], 'ee'),
	 (['a'], 'fg'),
	 (['b'], 'eh')]
)
def test_filter_substr_empty(keys, value):
	r = h.filter_substr(keys, value, [{'a': 'abcd', 'b': 'cdef'}, {'a': 'acc', 'b': 'bdd'}, {'a': 'abd', 'b': 'cdf'}, {'a': 'cd', 'b': 'ef'}])
	assert(not r)
