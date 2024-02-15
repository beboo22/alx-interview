#!/usr/bin/python3
"""
Main file for testing
"""

def minOperations(n):
    # def countOPR(curent, cpy, opr):
    #     nonlocal result
    #     if curent == n:
    #         result = min(result, opr)
    #         return result
    #     if cpy > 0:
    #         countOPR(curent + 1, cpy, opr +1)
    #     countOPR(curent + 1, cpy, opr +1)
    if (n < 2):
        return 0
    opr = 1
    curent = 1
    result = float(1000000000000000000)
    for x in range(n):
        if curent == n:
            result = min(result, opr)
            return result
        if n % 2 == 0:
            n = n / 2
            
        else:
            opr += 1
            curent += 1

    
    # countOPR(1, 1, 1)
    return result
