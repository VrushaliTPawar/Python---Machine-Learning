"""
    Que: Write a program to display:
        Value
        Type
        Memory address
    for a variable using appropriate built-in function.
"""

# Example 1:
num = 10
print(num)          # 10
print(type(num))    # <class 'int'>
print(id(num))      # 140718514750872

x = 10
print(num)          # 10
print(type(num))    # <class 'int'>
print(id(num))      # 140718514750872 - Same as that of num becasue both num and x has same value and hence points to same memory address.

#Example 2:
num = "Jay Ganesh...."
print(num)          # Jay Ganesh....
print(type(num))    # <class 'str'>
print(id(num))      # 2858918969968

