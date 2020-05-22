'''
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
'''


'''
SOLUTIONS:
1) Brute force: iterate over input_list using three nested for loops.
    Time complexity is : O(n^3). Space complexity is constant: O(1).
2) First of all I sort input_list. The highest product of three elements of a sorted list is either the product of the last three elements (which are the three largest ones) or the product of the first two     elements and the last one (in case the first two elements are negative). After calculating this two products, I return the max of them.
    Time complexity is O(nlogn) because that is the runtime of the fastest sorting algorithm. Space complexity is O(logn), because sorting algorithms require logn space.
3) Same as solution 2 but without using a sorting algorithms. Instead, I use a greedy approach. Time complexity is O(n) and space complexity is O(1).

'''

'''
# Solution 2:
def highest_product_of_3(input_list):
  input_list.sort()
  return max(input_list[0] * input_list[1] * input_list[-1], input_list[-3] * input_list[-2] * input_list[-1])
'''

# Solution 3:
import math
def highest_product_of_3(input_list):

  if len(input_list) < 3:
    raise ValueError('Less than 3 items!')

  min_1 = math.inf
  min_2 = math.inf
  max_1 = -math.inf
  max_2 = -math.inf
  max_3 = -math.inf

  for num in input_list:
    if num <= min_1:
      min_2 = min_1
      min_1 = num
    elif num <= min_2:
      min_2 = num

    if num >= max_1:
      max_3 = max_2
      max_2 = max_1
      max_1 = num
    elif num >= max_2:
      max_3 = max_2
      max_2 = num
    elif num >= max_3:
      max_3 = num

  return max(max_1 * max_2 * max_3, min_1 * min_2 * max_1)

my_list = [6, 1, 3, 5, 7, 8, 2]
my_list = [-5, -1, -3, -2]
print(highest_product_of_3(my_list))