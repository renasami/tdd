import unittest
from red_roman import to_roman

class TestToRoman(unittest.TestCase):
    
    # エラーケースのテスト
    def test_invalid_zero(self):
        with self.assertRaises(ValueError):
            to_roman(0)

    def test_invalid_negative(self):
        with self.assertRaises(ValueError):
            to_roman(-1)

    def test_invalid_over_max(self):
        with self.assertRaises(ValueError):
            to_roman(4000)

    # 正常ケースのテスト
    def test_minimum_value(self):
        self.assertEqual(to_roman(1), "I")

    def test_value_4(self):
        self.assertEqual(to_roman(4), "IV")

    def test_value_9(self):
        self.assertEqual(to_roman(9), "IX")

    def test_value_40(self):
        self.assertEqual(to_roman(40), "XL")

    def test_value_50(self):
        self.assertEqual(to_roman(50), "L")

    def test_value_90(self):
        self.assertEqual(to_roman(90), "XC")

    def test_value_100(self):
        self.assertEqual(to_roman(100), "C")

    def test_value_400(self):
        self.assertEqual(to_roman(400), "CD")

    def test_value_500(self):
        self.assertEqual(to_roman(500), "D")

    def test_value_900(self):
        self.assertEqual(to_roman(900), "CM")

    def test_value_58(self):
        self.assertEqual(to_roman(58), "LVIII")

    def test_value_1994(self):
        self.assertEqual(to_roman(1994), "MCMXCIV")

    def test_maximum_value(self):
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        
if __name__ == '__main__':
    unittest.main()
