'''
My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down cake-eating experience.

I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
Each customer order (from either register) as it was finished by the kitchen. (served_orders)
Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

We'll represent each customer order as a unique integer.

As an example,

  Take Out Orders: [1, 3, 5]
  Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]

would not be first-come, first-served, since order 3 was requested before order 5 but order 5 was served first.

But,

  Take Out Orders: [17, 8, 24]
  Dine In Orders: [12, 19, 2]
  Served Orders: [17, 8, 12, 19, 24, 2]

would be first-come, first-served.

Note: Order numbers are arbitrary. They do not have to be in increasing order.
'''



'''
1st SOLUTION:
I iterate over take_out_orders list, checking that the index of its elements in served_orders are ascending. Then, I do the same for dine_in_orders: I check that the index of its elements in served_orders are ascending. If at least one check is not successful, I return False.

Time: O(n^2)
  because I need to use index() method (linear time complexity) inside a for loop.

Space: O(n)
  The linear space complexity is due to the sets that I need to create.

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    if len(take_out_orders) + len(dine_in_orders) != len(served_orders):
        return False

    take_out_set = set(take_out_orders)
    dine_in_set = set(dine_in_orders)
    served_orders_set = set(served_orders)
    is_subset = take_out_set.issubset(served_orders_set) and dine_in_set.issubset(served_orders_set)
    if not is_subset:
        return False

    current_index = 0
    for i, order in enumerate(dine_in_orders):
        if served_orders.index(order) < current_index:
            return False
        else:
          current_index = served_orders.index(order)

    current_index = 0
    for j, order in enumerate(take_out_orders):
        if served_orders.index(order) < current_index:
            return False
        else:
            current_index = served_orders.index(order)

    return True
'''

'''
2nd Solution:
  First, I check that the sum of the lengths of take_out_orders and dine_in_orders lists is equal to the length of served_orders list.
  Then I iterate through served_orders and check that the current order in served_orders is either the first order of take_out_orders or dine_in_orders. If that is NOT the case, I return False, because it means that the orders are not served on a first-come, first-served basis. If that is the case, I increment by one the index of either take_out_orders or dine_in_orders.
  Please check the code below, it explains the thought process clearer than words can do.

  This solution is more efficient than the 1st one because it's linear time and constant space.
  Time: O(n)
  Space: O(1)
'''

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

  if len(take_out_orders) + len(dine_in_orders) != len(served_orders):
    return False

  current_index_take_out = 0
  current_index_dine_in = 0

  for order in served_orders:
    if order != dine_in_orders[current_index_dine_in] and order != take_out_orders[current_index_take_out]:
      return False
    elif order == dine_in_orders[current_index_dine_in] and current_index_dine_in + 1 != len(dine_in_orders):
      current_index_dine_in += 1
    elif order == take_out_orders[current_index_take_out] and current_index_take_out + 1 != len(take_out_orders):
      current_index_take_out += 1
  return True


take_out_orders = [1, 5, 3]
dine_in_orders = [2, 4, 6]
served_orders = [1, 2, 4, 6, 5, 3]
print(is_first_come_first_served(dine_in_orders, take_out_orders, served_orders))


