import pytest
from companion import matches as m


@pytest.mark.parametrize(
	['id_', 'live', 'res'],
	[('1', True, '/live'),
	 ('1', False, '/matches/1'),
	 (None, False, '/proMatches')
	]
)
def test_endpoint(id_, live, res):
	r = m.endpoint(id_, live)
	assert(r == res)
