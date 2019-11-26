# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.

def get_perfect(value):
    value = str(value)
    tmp = 0

    for ch in value:
        # what to do when the value is over 10?  Do I just return the subset?
        if tmp + int(ch) > 10:
            return str(tmp) + str(10 - tmp)
        tmp = tmp + int(ch)

    return value + str(10 - tmp)


if __name__ == "__main__":
    
    print(get_perfect(1))
    print(get_perfect(10))
    print(get_perfect(12))
    print(get_perfect(19))
    print(get_perfect(99))
    print(get_perfect(999))