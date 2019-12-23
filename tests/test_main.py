import unittest

from apps.main import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    fizzbuzz = fizzbuzz()

    def test_1を渡したら文字列1を返す(self):
        self.assertEqual('1', fizzbuzz.convert(1))

    def test_2を渡したら文字列2を返す(self):  # 三角測量(Triangulation)
        self.assertEqual('2', fizzbuzz.convert(2))

    def test_3を渡したら文字列Fizzを返す(self):
        self.assertEqual('Fizz', fizzbuzz.convert(3))

    def test_6を渡したら文字列Fizzを返す(self):
        self.assertEqual('Fizz', fizzbuzz.convert(6))
