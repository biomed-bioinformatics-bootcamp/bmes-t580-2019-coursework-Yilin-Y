# This is the play code for the factorial calculation

# the factorial calculation:
# 5! = 120;
# 5! = 5 * 4 * 3 * 2 * 1


def factorial(n): # set the function for factorial calculation
    if n == 1:
        return 1

    return n * factorial(n - 1)

# the print format of the factorial calculation
print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),  # 120
    factorial(3),  # 6
    factorial(11)  # HUGE
))


# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(limit): # the function of the Fibonacci in the factorial calculation
    nums = []

    current = 0
    next = 1

    while current < limit: # if the current number is smaller than the limit number, use the next number of the current number
        current, next = next, next + current
        nums.append(current)

    return nums


print('via lists')
for n in fibonacci(100):
    print(n, end=', ')

print()


def fibonacci_co(): # use the function to find the yield of the fibonacci
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current


print('with yield')
for n in fibonacci_co():
    if n > 1000:
        break

    print(n, end=', ')