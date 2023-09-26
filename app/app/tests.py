"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test subtract numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

    def test_add_and_sub(self):
        """Test add and subtract function together"""
        res1 = calc.add(1, 2)
        res2 = calc.subtract(1, 2)

        self.assertEqual(res1, 3)
        self.assertEqual(res2, 1)
