'''
Write a function fib() that takes an integer n and returns the nth Fibonacci number.

Let's say our Fibonacci series is 0-indexed and starts with 0. So:

  fib(0)  # => 0
  fib(1)  # => 1
  fib(2)  # => 1
  fib(3)  # => 2
  fib(4)  # => 3
  ...

'''

'''
Solution 1:
  Using recursion, I can reduce the given problem to many simpler subproblems.

  Time: O(2^n)
  Space: O(n) The space complexity is the size of the call stack, which never grows larger than n, because there pops and pushes kinda balance each others (I know, this is not the most scientific explanation!). The linear space complexity is easier to prove drawing the recursion tree and the call stack.


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
'''


'''
Solution 2:
  We store the return values of each call in a dictionary, so that I don't need to make multiple calls with the same argument.

  Time: O(n)
  Space: O(n)
'''


def fib(n):
    if n == 0 or n == 1:
        return n

    cache = {0: 0, 1: 1}
    for i in range(2, n + 1):
        # As we are in an ascending for loop (from 2 to n + 1), if i - 1 is in the dictionary also i - 2 will be --> There is no need to formally check that i - 2 is in the dictionary.
        if i - 1 in cache:
            cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n - 1] + cache[n - 2]


'''
Solution 3:
  We use a bottom-up approach, starting from 0 until we get to n.

  Time: O(n)
  Space: O(1)


def fib(n):
    if n == 0 or n == 1:
        return n

    before_prev = 0
    prev = 1

    # when we don't need the index, in Python we can use _, which means that we don't care about i.
    for _ in range(n - 1):
        current = prev + before_prev
        before_prev = prev
        prev = current

    return current
'''


print("n = 0, fib =", fib(0))
print("n = 1, fib =", fib(1))
print("n = 2, fib =", fib(2))
print("n = 3, fib =", fib(3))
print("n = 4, fib =", fib(4))
print("n = 5, fib =", fib(5))
# Running the function with a large enough input, like fib(37), we can see the huge difference in runtime between O(n^2) of solution 1 and O(n) of solution 2 and 3.
print("n = 6, fib =", fib(37))
