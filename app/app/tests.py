"""
Sample tests 
"""

from django.test import SimpleTestCase

from app import calc 

class CalcTest(SimpleTestCase):
    """Test de Calc module."""
    
    def test_add_numbers(self):
        """Teste ading numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res,11)

    def test_subtract_numbers(self):
        """Test subtracing numbers together"""
        res = calc.subtract(5,6)
        self.assertEqual(res,-1)