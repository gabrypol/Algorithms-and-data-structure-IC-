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
import unittest

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

class Test(unittest.TestCase):

  def test_small_list(self):
    actual = get_products_of_all_ints_except_at_index([1, 2, 3])
    expected = [6, 3, 2]
    self.assertEqual(actual, expected)

  def test_longer_list(self):
    actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
    expected = [120, 480, 240, 320, 960, 192]
    self.assertEqual(actual, expected)

  def test_list_has_one_zero(self):
    actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
    expected = [0, 0, 36, 0]
    self.assertEqual(actual, expected)

  def test_list_has_two_zeros(self):
    actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
    expected = [0, 0, 0, 0, 0]
    self.assertEqual(actual, expected)

  def test_one_negative_number(self):
    actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
    expected = [32, -12, -24]
    self.assertEqual(actual, expected)

  def test_all_negative_numbers(self):
    actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
    expected = [-8, -56, -14, -28]
    self.assertEqual(actual, expected)

  def test_error_with_empty_list(self):
    with self.assertRaises(Exception):
      get_products_of_all_ints_except_at_index([])

  def test_error_with_one_number(self):
    with self.assertRaises(Exception):
      get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)