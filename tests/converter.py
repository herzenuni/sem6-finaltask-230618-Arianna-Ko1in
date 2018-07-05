import pytest
import main

class Converter:
    def testtypesbin(self):
        assert main.get_basement('bin')==2

    def testtypesoct(self):
        assert main.get_basement('oct')==8

    def testtypeshex(self):
        assert main.get_basement('hex')==16

    @pytest.mark.skip(reason='inner function')
    @main.converted
    def test_converted_2_inner(self, basement, number):
        assert basement == 2 and number == '1110'

    def test_converted_2(self):
        self.test_converted_2_inner(2, 14)

    @pytest.mark.skip(reason='inner function')
    @main.converted
    def test_converted_8_inner(self, basement, number):
        assert basement == 8 and number == '110'

    def test_converted_8(self):
        self.test_converted_8_inner(8, 72)

    @pytest.mark.skip(reason='inner function')
    @main.converted
    def test_converted_16_inner(self, basement, number):
        assert basement == 16 and number == '110'

    def test_converted_16(self):
        self.test_converted_16_inner(16, 272)
