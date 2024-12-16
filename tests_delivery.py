from delivery import calculate_delivery_cost
import unittest
from parameterized import parameterized
from concurrent.futures import ThreadPoolExecutor

def run_test(test_case):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner().run(suite)

class TestDeliveryCost(unittest.TestCase):
    @parameterized.expand([
        (1.5, 'small', True, 'very_high', 720),
        (1.5, 'big', False, 'high', 400),
        (2, 'small', False, 'increased', 400),
        (2.1, 'big', True, 'normal', 600),
        (10, 'small', True, 'very_high', 800),
        (10.1, 'big', False, 'high', 560),
        (30, 'small', True, 'increased', 720),
        (30.1, 'big', False, 'normal', 500),
    ])
    def test_delivery_cost(self, distance, size, fragile, load, expected):
        self.assertEqual(calculate_delivery_cost(distance, size, fragile, load), expected)

class TestDeliveryCostNegative(unittest.TestCase):
    @parameterized.expand([
        (-1, 'small', True, 'very_high', "Distance must be a positive number."),
        (0, 'small', True, 'very_high', "Distance must be a positive number."),
        (10, 'medium', True, 'very_high', "Size must be 'small' or 'big'."),
        (10, 'small', None, 'very_high', "Fragility must be True or False."),
        (10, 'small', True, 'heavy', "Load must be one of: 'very_high', 'high', 'increased', 'normal'."),
        (31, 'big', True, 'normal', "Fragile goods cannot be transported over 30 km."),
    ])
    def test_invalid_cases(self, distance, size, fragile, load, expected_message):
        with self.assertRaises(ValueError) as context:
            calculate_delivery_cost(distance, size, fragile, load)
        self.assertEqual(str(context.exception), expected_message)

if __name__ == '__main__':
    tests = [TestDeliveryCost, TestDeliveryCostNegative]
    with ThreadPoolExecutor() as executor:
        executor.map(run_test, tests)
