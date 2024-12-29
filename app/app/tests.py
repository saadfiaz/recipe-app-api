from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test Adding numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    
    def test_subtract_number(self):
        """Test Subtracting number"""  
        res = calc.subtract(15, 10)
        self.assertEqual(res, 5)
