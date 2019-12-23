import unittest

from apps.main import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    fizzbuzz = fizzbuzz()

    def test_数を文字列にして返す_1を渡したら文字列1を返す(self):
        self.assertEqual('1', fizzbuzz.convert(1))

    def test_3の倍数のときは数の代わりにFizzと返す_3を渡したら文字列Fizzを返す(self):
        self.assertEqual('Fizz', fizzbuzz.convert(3))

    def test_5の倍数のときはBuzzと返す_5を渡したら文字列Buzzを返す(self):
        self.assertEqual('Buzz', fizzbuzz.convert(5))
