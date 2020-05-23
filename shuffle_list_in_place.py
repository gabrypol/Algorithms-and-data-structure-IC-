'''
Write a function for doing an in-place shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
'''

'''
Solution:
  I iterate through the input list and at each iteration I select randomly one index in the range(current_iteration_index, index_of_last_element_of_the_list). Then, I swap the element at index i (current iteration) with the element at the randomly generated index.
  This is done in place, since I haven't allocated any additional space in memory.
'''

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle_in_place(my_list):
    if len(my_list) <= 1:
        return my_list

    for i in range(len(my_list)):
        idx_to_be_moved = get_random(i, len(my_list) - 1)
        my_list[i], my_list[idx_to_be_moved] = my_list[idx_to_be_moved], my_list[i]

    return my_list

sample_list = [1, 2, 3, 4, 5]
print(shuffle_in_place(sample_list))

'''
  Time complexity: O(n)
  Space complexity: O(1) because the list is shuffled in place.
'''