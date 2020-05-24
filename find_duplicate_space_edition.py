'''
Find a duplicate, Space Edition™.

We have a list of integers, where:

The integers are in the range 1..n1..n
The list has a length of n+1
It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip MacBook Pro With Retina Display™. Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. So we need to optimize for space!
'''


def find_repeat(numbers):
  numbers.sort()
  for i, num in enumerate(numbers[1:], 1):
    if numbers[i] == numbers[i - 1]:
      return num

my_list = [4, 1, 4, 8, 3, 2, 7, 6, 5]
print(find_repeat(my_list))

'''
Time: O(nlogn)
Space: O(1)
'''