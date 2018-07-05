import pytest
import main

class TestNames:
    def test_correct_number(self):
        assert main.get_name(1)=='one'

    def test_outofrange_number(self):
        assert main.get_name(-1) == False

    def test_outofrange_number_2(self):
        assert main.get_name(10) == False

