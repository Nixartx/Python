import unittest
import anagrams


class AnagramsTest(unittest.TestCase):
    __cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("12345 6789a", "12345 6789a"),
        ("", ""),
    ]

    def test_rev(self):
        for case in self.__cases:
            with self.subTest(case=case):
                self.assertEqual(anagrams.rev(case[0]), case[1])