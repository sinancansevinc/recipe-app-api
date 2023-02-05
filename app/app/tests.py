"""
Sample test
"""
from django.test import SimpleTestCase
from . import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    
    def test_add_numbers(self):
        result = calc.add(5,4)
        
        self.assertEqual(result,9)
        
    def test_multiply_numbers(self):
        result = calc.multiply(4,3)
        self.assertEqual(result,12)
        
    def test_subtract_numbers(self):
        """Test substracting module"""
        res = calc.subtract(5,12)
        self.assertEqual(res,7)