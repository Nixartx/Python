from collections import Counter
from functools import lru_cache


class CountUnique:

    @lru_cache
    def count(self, string):
        count_of_unique = 0
        for letter, count in Counter(string).most_common()[::-1]:
            if count == 1:
                count_of_unique += 1
            if count > 1:
                break
        return count_of_unique


if __name__ == '__main__':
    a = CountUnique()
    print(a.count("asasdasd asdasd kjm"))
    print(a.count("asasdasd asdasd"))
    print(a.count("asasdasd asdasd kjm"))
    print(a.count("12345 6789a"))
    print(a.count("@^%#$^"))
    print(a.count())
    # print(a.count(123))

    print(a.count.cache_info()[1])
