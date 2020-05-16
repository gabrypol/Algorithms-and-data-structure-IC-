'''
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

For example:

  my_list     = [3, 4, 6, 10, 11, 15]
  alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
'''

def merge_lists(my_list, alices_list):

  merged_list = []
  my_list_current_idx = 0
  alices_list_current_idx = 0

  if len(my_list) == 0:
    return alices_list

  if len(alices_list) == 0:
    return my_list

  while len(merged_list) <= len(my_list) + len(alices_list):
    if my_list[my_list_current_idx] <= alices_list[alices_list_current_idx]:
      merged_list.append(my_list[my_list_current_idx])
      if my_list_current_idx != len(my_list) - 1:
        my_list_current_idx += 1
      else:
        merged_list += alices_list[alices_list_current_idx:]
        return merged_list
    else:
      merged_list.append(alices_list[alices_list_current_idx])
      if alices_list_current_idx != len(alices_list) - 1:
        alices_list_current_idx += 1
      else:
        merged_list += my_list[my_list_current_idx:]
        return merged_list


my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, alices_list))


'''
Time: O(n)
Space: O(n)
'''