'''
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution!
'''

'''
Solution 1: Brute force. I can iterate over the given list, and nest another loop inside which multiplies the elements of the list not at index i. 
  Time complexity: O(n^2)
  Space complexity: O(n)

Most likely we can do it faster than O(n^2)...
Solution 2:
  Time complexity: O(n)
  Space complexity: O(n)
'''

# Solution 2
def get_products_of_all_ints_except_at_index(my_list):

  if len(my_list) < 2:
    raise ValueError('The list has less than two elements')

  output_list = [None] * len(my_list)
  current_product_before = 1
  for i, num in enumerate(my_list):
    output_list[i] = current_product_before
    current_product_before *= num

  current_product_after = 1
  for i in range(len(my_list) - 1, -1, -1):
    output_list[i] *= current_product_after
    current_product_after *= my_list[i]

  return output_list


my_input = [1, 7, 5, 6, 2]
print(get_products_of_all_ints_except_at_index(my_input))