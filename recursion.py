#### recursion function to calculate factorial: n! #########
def get_recursive_factorial(n):
    if n < 0 :
        return -1
    elif n < 2:
        return 1
    else:
        return n*get_recursive_factorial(n-1)


print(get_recursive_factorial(5))