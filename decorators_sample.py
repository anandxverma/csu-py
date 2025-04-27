def aFunction(n: int) -> int:
    """
    This function takes an integer n and returns the sum of all integers from 1 to n.
    """
    if (n <= 0):
        return "Sample string output"
    return sum(range(1, n + 1))

print(aFunction(5))  # Output: 15
print(aFunction(0))  # Output: Sample string output

def simple_decorator(func):
    """
    A simple decorator that prints the function name and its arguments.
    """
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def arbit_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

arbit_args(1, 2, key1="value1", key2="value2")