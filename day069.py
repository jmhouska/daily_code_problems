# This problem was asked by Facebook.
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.
import bisect
import math

def get_max(items):
    positives = []
    negatives = []

    for item in items:
        if item == 0:
            return 0
        elif item > 0:
            bisect.insort(positives, item)
        else: 
            bisect.insort(negatives, item)
    
    if len(negatives) == 0 or (len(negatives) == 1 and len(positives) > 2) or (len(negatives) > 1 and len(positives) > 1 and negatives[-1] * negatives[-2] < positives[-1] * positives[-2]):
        return math.prod(positives[-3:])
    elif (len(negatives) > 1 and len(positives) == 1) or (len(negatives) > 1 and negatives[-1] * negatives[-2] > positives[-1] * positives[-2]):
        return math.prod([negatives[0], negatives[1], positives[-1]])
    elif len(negatives) == 1 and len(positives) == 2:
        return math.prod([negatives[-1], positives[0], positives[1]])

    else:
        raise Exception("This should not happen...")
    

if __name__ == "__main__":
    print(get_max([10, 10, 5, 2, 2]), 'This should be 500')
    print(get_max([10, -10, 5, 2, 2]), 'This should be 500')
    print(get_max([-1, -1, 5, 2, 2]), 'This should be 20')

    print(get_max([-10, -10, 5, 2, 2]), 'This should be 500')
    print(get_max([-10, -10, -5, 2]), 'This should be 200')
    print(get_max([-10, 5, 2, 2]), 'This should be 20')
