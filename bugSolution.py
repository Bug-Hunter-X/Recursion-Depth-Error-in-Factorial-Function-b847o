def my_function_iterative(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

print(my_function_iterative(5)) # Example usage