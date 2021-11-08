from collections import Counter
from functools import lru_cache


class CountUnique:

    @lru_cache
    def count(self, string):
        count_of_unique = 0
        for count in Counter(string).values():
            if count == 1:
                count_of_unique += 1
        return count_of_unique
