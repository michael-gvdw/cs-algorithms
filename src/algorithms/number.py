
'''
Title: fibonacci
Complexity: O(n)

Description:
    The Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
    In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
    Fn = Fn-1 + Fn-2

    with seed values  
    F0 = 0 and F1 = 1.
'''
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


'''
Title: factorial
Complexity: O(n)

Description:
    In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n:
    n!=n * (n-1) * (n-2) * (n-3) ... * 3 * 2 * 1

    For example,
    5!=5 * 4 * 3 * 2 * 1 = 120
'''
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

    
