"""
    Que: Why does the input() function always returns a string?
    How can you convert it to another data type?
"""

"""
    Ans:
        -> The input() function reads data entered from the keyboard as text. 
        -> Since keyboard input is received as characters, Python returns it as a str object.
        -> Even though you entered a number, Python treats it as the string "25".

        -> by doing type casting, we can convert it to another data type
"""

print("Enter age :")
age = input() # Here output of input() gets stored into age and input() returns string default.

print(age)          # 24
print(type(age))    # <class 'str'> 


# Type casting
print("Enter age :")
age = int(input()) # Type casting : string to int.

print(age)          # 24
print(type(age))    # <class 'int'>

