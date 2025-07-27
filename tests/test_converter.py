import unittest
from converter import tagalog_number, tagalog_number_to_digits

class TestTagalogNumberConverter(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(tagalog_number(0), "sero")
        self.assertEqual(tagalog_number(1), "isa")
        self.assertEqual(tagalog_number(5), "lima")
        self.assertEqual(tagalog_number(10), "sampu")
    
    def test_teens(self):
        self.assertEqual(tagalog_number(11), "labing-isa")
        self.assertEqual(tagalog_number(15), "labinlima")
        self.assertEqual(tagalog_number(19), "labinsiyam")
    
    def test_tens(self):
        self.assertEqual(tagalog_number(20), "dalawampu")
        self.assertEqual(tagalog_number(25), "dalawampu't lima")
        self.assertEqual(tagalog_number(50), "limampu")
        self.assertEqual(tagalog_number(99), "siyamnapu't siyam")
    
    def test_hundreds(self):
        self.assertEqual(tagalog_number(100), "isang daan")
        self.assertEqual(tagalog_number(200), "dalawang daan")
        self.assertEqual(tagalog_number(123), "isang daan at dalawampu't tatlo")
        self.assertEqual(tagalog_number(555), "limang daan at limampu't lima")
    
    def test_thousands(self):
        self.assertEqual(tagalog_number(1000), "isang libo")
        self.assertEqual(tagalog_number(2000), "dalawang libo")
        self.assertEqual(tagalog_number(1234), "isang libo't dalawang daan at tatlumpu't apat")
        self.assertEqual(tagalog_number(9999), "siyam na libo't siyam na daan at siyamnapu't siyam")
    
    def test_millions(self):
        self.assertEqual(tagalog_number(1000000), "isang milyon")
        self.assertEqual(tagalog_number(2000000), "dalawang milyon")
        self.assertEqual(tagalog_number(1234567), "isang milyon dalawang daan at tatlumpu't apat na libo't limang daan at animnapu't pito")
    
    def test_billions(self):
        self.assertEqual(tagalog_number(1000000000), "isang bilyon")
        self.assertEqual(tagalog_number(2000000000), "dalawang bilyon")
    
    def test_invalid_input(self):
        self.assertEqual(tagalog_number(-1), "Negative numbers are not supported.")
        self.assertEqual(tagalog_number(1.5), "Input must be an integer.")
    
    def test_reverse_conversion(self):
        self.assertEqual(tagalog_number_to_digits("sero"), 0)
        self.assertEqual(tagalog_number_to_digits("isa"), 1)
        self.assertEqual(tagalog_number_to_digits("dalawampu't lima"), 25)
        self.assertEqual(tagalog_number_to_digits("isang daan at dalawampu't tatlo"), 123)
        self.assertEqual(tagalog_number_to_digits("isang libo't dalawang daan at tatlumpu't apat"), 1234)

if __name__ == '__main__':
    unittest.main()