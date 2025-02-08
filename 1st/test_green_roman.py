import unittest
from green_roman import to_roman

class TestRomanConverter(unittest.TestCase):
    def test_1(self):
        self.assertEqual(to_roman(1), "I")

    def test_2(self):
        self.assertEqual(to_roman(2), "II")

    def test_3(self):
        self.assertEqual(to_roman(3),"III")

    def test_4(self):
        self.assertEqual(to_roman(4),"IV")
    
    def test_5(self):
        self.assertEqual(to_roman(5),"V")
    
    def test_6(self):
        self.assertEqual(to_roman(6),"VI")
    
    def test_7(self):
        self.assertEqual(to_roman(7),"VII")
    
    def test_8(self):
        self.assertEqual(to_roman(8),"VIII")

    def test_9(self):
        self.assertEqual(to_roman(9),"IX")

if __name__ == "__main__":
    unittest.main()
