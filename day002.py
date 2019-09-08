# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

from functools import reduce

if __name__ == "__main__":
    in1 = [1,2,3,4,5]
    in2 = [3,2,1]
    product = reduce(lambda x,y: x*y, in1)
    out = [int(product / i) for i in in1]
    print(out)
    product = reduce(lambda x,y: x*y, in2)
    out = [int(product / i) for i in in2]
    print(out)

    out = [reduce(lambda x, y: x * y, in1[:i] + in1[i + 1:]) for i in range(len(in1))]
    print(out)

    out = [reduce(lambda x, y: x * y, in2[:i] + in2[i + 1:]) for i in range(len(in2))]
    print(out)