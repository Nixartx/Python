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
        for text, reversed_text in self.__cases:
            with self.subTest(msg="Checking if text is reverted reversed_text", text=text,reversed_text=reversed_text):
                self.assertEqual(anagrams.rev(text), reversed_text)