"""
    Que: Predict the output:
        a = 10
        b = 10
        print(id(a) == id(b))
    Explain why this happens.
"""

a = 10
b = 10
print(id(a) == id(b))   # True
print(id(a))    # 140721821500824
print(id(b))    # 140721821500824

"""
    Ans:
        -> True
        -> because both a and b refer to the same integer object in memory.
"""