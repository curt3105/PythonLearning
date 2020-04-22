import unittest

class TestCase(unittest.TestCase):
    def test_variable_can_change_type(self):
        number_two = 2
        assert type(number_two) == int