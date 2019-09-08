# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.
import math

def gen_out(minimum, next_minimum, max_val):
    if next_minimum - minimum < 2:
        return max_val + 1
    else:
        return minimum + 1

def find_vals (arr):
    a = [math.inf, math.inf, -math.inf]
    for i in arr:
        # set the min val seen
        if  i < 1:
            continue

        if i < a[0]:
            a[0] = i
        # set the next min val
        elif i < a[1] and i != a[0]:
            a[1] = i
        
        # set the max val
        if i > a[2]:
            a[2] = i
    
    return a

if __name__ == "__main__":
    arr = [3, 4, -1, 1]
    print(gen_out(*find_vals(arr)))
    
    arr = [1, 2, 0]
    print(gen_out(*find_vals(arr)))
    
    arr = [1, 4, 0]
    print(gen_out(*find_vals(arr)))
