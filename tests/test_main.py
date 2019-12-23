import unittest

from apps.main import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    # 前準備
    fizzbuzz = fizzbuzz()

    def test_1を渡したら文字列1を返す(self):
        # 実行
        # 検証
        self.assertEqual('1', fizzbuzz.convert(1))
