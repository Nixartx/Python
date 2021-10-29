import unittest
import anagrams


class AnagramsTest(unittest.TestCase):
    __cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("12345 6789a", "12345 6789a"),
        ("", ""),
    ]

    def test_string_reverse_success(self):
        for text, reversed_text in self.__cases:
            with self.subTest(msg="Checking if reversed_text is reverted text", text=text, reversed_text=reversed_text):
                self.assertEqual(anagrams.string_reverse(text), reversed_text)

    def test_string_reverse_exception(self):
        with self.assertRaises(AttributeError):
            anagrams.string_reverse(12345)
