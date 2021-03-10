"""
Unit testing the calculator app
"""

import calculator


class TestCalculator:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)
