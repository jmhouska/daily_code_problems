# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

if __name__ == "__main__":
   k = 17
   arr = [10, 15, 3, 7]
   for x in range(len(arr)):
       for y in arr[x:]:
           if (arr[x] + y) == k:
               print(y, arr[x])
               print(True)
               break