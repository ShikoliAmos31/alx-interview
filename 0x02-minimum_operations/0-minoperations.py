#!/usr/bin/python3
""" Module for 0-minoperations """

def minOperations(n):
    """
    minOperations
    Gets fewest number of operations needed to result in exactly n H characters
    """
    # If n is less than 2, it's impossible to achieve more than 1 'H'
    if n < 2:
        return 0
    
    ops, root = 0, 2
    
    while root <= n:
        # While n is divisible by root, apply the operations
        while n % root == 0:
            ops += root
            n //= root
        root += 1
        
    return ops
