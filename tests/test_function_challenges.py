import unittest
from unittest.mock import patch, Mock
from functions_challenges import get_float, miles_to_km, relay_distance, relay_distance_input

input_mock = Mock()


class TestCase(unittest.TestCase):

    @patch('builtins.input', input_mock)
    def test_get_float(self):
        test_cases = [
            # (input_from_user, expected_float)
            ("9", 9.0),
            ("9.0", 9.0),
            ("3.14", 3.14),
            ("0.0", 0.0)
        ]

        for float_from_input, expected in test_cases:
            with self.subTest(float_from_input=float_from_input):
                input_mock.side_effect = [float_from_input]
                result = get_float(float_from_input)
                self.assertEqual(result, expected,
                    msg=f"The input {float_from_input} resulted in returning a value of type {type(result)} instead of a float!")


    def test_miles_to_km(self):
        test_cases = [
            # (miles, expected_km)
            (1, 1.60934),
            (3, 4.82802),
            (5, 8.0467)
        ]
        
        for miles, expected_km in test_cases:
            with self.subTest(miles=miles):
                result = miles_to_km(miles)
                self.assertEqual(result, expected_km, msg=f"Expecting {miles} mile(s) to be equal to {expected_km} kilometers")


    def test_relay_distance(self):
        test_cases = [
            # (distance_per_runner, number_of_runners, expected_distance_km)
            (1, 2, 2),
            (3, 4, 12),
            (0.5, 1, 0.5)
        ]

        for distance_per_runner, number_of_runners, expected_distance_km in test_cases:
            with self.subTest(
                distance_per_runner=distance_per_runner,
                number_of_runners=number_of_runners,
                expected_distance_km=expected_distance_km
            ):
                result = relay_distance(distance_per_runner, number_of_runners)
                self.assertEqual(result, expected_distance_km,
                    msg=f"{distance_per_runner} * {number_of_runners} resulted in returning a value of {result}! The correct answer was {expected_distance_km}!")


    @patch('builtins.input', input_mock)
    def test_relay_distance_input(self):
        test_cases = [
            # (runners, miles_per_runner, expected_km)
            ("4", "5", 32.1868),      # 4 * 5    * 1.60934 = 32.1868
            ("2", "10", 32.1868),     # 2 * 10   * 1.60934 = 32.1868
            ("8", "1", 12.87472),     # 8 * 1    * 1.60934 = 12.87472
            ("1", "26.2", 42.164708), # 1 * 26.2 * 1.60934 = 42.164708
            ("6", "0.5", 4.82802)     # 6 * 0.5  * 1.60934 =  4.82802
        ]
        
        for runners, miles, expected in test_cases:
            with self.subTest(runners=runners, miles=miles):
                input_mock.side_effect = [runners, miles]
                result = relay_distance_input()
                self.assertAlmostEqual(result, expected,
                    msg=f"With {runners} runners running {miles} miles each, expected {expected} km but got {result}")