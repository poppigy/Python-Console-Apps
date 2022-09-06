version = 2


def isBadVersion(n: int) -> bool:
    if n >= version:
        return True
    return False


def firstBadVersion(n: int) -> int:
    min_ = 1
    max_ = n
    bad = (min_ + max_) // 2
    while min_ <= max_:
        if isBadVersion(bad):
            if not isBadVersion(bad - 1):
                return bad
            max_ = bad
            bad = (min_ + bad) // 2
        else:
            if isBadVersion(bad + 1):
                return bad + 1
            min_ = bad
            bad = (bad + max_) // 2
    return bad


if __name__ == '__main__':
    print(firstBadVersion(2))

