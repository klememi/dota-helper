import betamax
import pytest
from companion import players as p


with betamax.Betamax.configure() as config:
	config.cassette_library_dir = 'tests/fixtures/cassettes'


def test_player_id_not_ok(betamax_session):
	assert(p.player_id_is_ok(1) == False)
	assert(p.player_id_is_ok(2) == False)
	assert(p.player_id_is_ok(3) == False)
	assert(p.player_id_is_ok(4) == False)


def test_player_id_is_ok(betamax_session):
	assert(p.player_id_is_ok(488180047) == True)
	assert(p.player_id_is_ok(372183905) == True)
	assert(p.player_id_is_ok(381341959) == True)
