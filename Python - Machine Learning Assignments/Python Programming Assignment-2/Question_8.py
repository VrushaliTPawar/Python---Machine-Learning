"""
    Que: Predict the output:
    x = input("Enter number: ")
    print(type(x))
    Explain the reason.
"""

x = input("Enter number: ")
print(type(x))              # <class 'str'>

"""
    Ans:
        -> The input() function reads data entered from the keyboard as text. 
        -> Since keyboard input is received as characters, Python returns it as a str object.
"""
