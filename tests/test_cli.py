import pytest
from click.testing import CliRunner
from companion import cli


runner = CliRunner()


def test_cli_favourite():
	result = runner.invoke(cli, ['favourite'], obj={})
	assert 'Please choose either of -a/-r options.' in result.output


def test_cli_heroes_counter_no_name():
	result = runner.invoke(cli, ['heroes', '--counter'], obj={})
	assert 'Please specify hero.' in result.output
