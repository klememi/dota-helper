import pytest
from companion import heroes as h


@pytest.mark.parametrize(
	['name', 'best', 'meta', 'counter', 'res'],
	[('Axe', False, False, False, '/heroes'),
	 ('Axe', True, False, False, '/rankings?hero_id=2'),
	 ('Axe', False, True, False, '/heroStats'),
	 ('Axe', False, False, True, '/heroes/2/matchups')]
)
def test_endpoint(name, best, meta, counter, res):
	r = h.endpoint(name, best, meta, counter)
	assert(r == res)


@pytest.mark.parametrize(
	['attr', 'res'],
	[('agi', 'Agility'),
	 ('str', 'Strength'),
	 ('int', 'Intelligence')]
)
def test_primary(attr, res):
	r = h.primary(attr)
	assert(r == res)
