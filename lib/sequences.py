#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fibonacci_sequence = []
    
    for i in range(length):
        if i == 0:
            fibonacci_sequence.append(0)
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_value)
    
    print(fibonacci_sequence)

# Example usage
print_fibonacci(9)
