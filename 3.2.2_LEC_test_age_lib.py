# coding: utf-8

import pytest
from age_lib import line_is_correct, military_case


class TestAgeLib:
	def test_military_case(self):
		assert military_case(49) == 'военнослужащий'
		assert military_case(50) == 'пенсионеры'
		assert military_case(17) == 'не наш случай'
		assert military_case(6) == 'не наш случай'

		with pytest.raises(ValueError):
			military_case(17.5)


@pytest.mark.parametrize(
	'test_input,expected',
	[
		('011,24,аналитик', True),
		('011,24,аналитик\n', True),

		('011', False),
		('011,,', False),
		('011,24,', False),
		('011,24,\n', False),
		('011,двадцать четыре,аналитик', False),
		('011,24.0,аналитик', False),
		('', False),
	]
)
def test_line_is_correct(test_input, expected):
	assert line_is_correct(test_input) == expected
