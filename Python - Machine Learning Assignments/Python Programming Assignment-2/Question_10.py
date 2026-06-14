"""
    Que: What will be the output?
    print("10" + "20")
    print(10+20)
    Explain the difference
"""

print("10" + "20")      # 1020
"""
    Ans:
    String Addition ("10" + "20")
    Both values are strings (str).
    The + operator joins (concatenates) strings
"""


print(10+20)            # 30
"""
    Ans: 
    Integer Addition (10 + 20)
    Both values are integers (int).
    The + operator performs mathematical addition
"""

#print("10" + 20)    # Error : TypeError: can only concatenate str (not "int") to str
"""
    Important: Python does not automatically convert between strings and integers.
"""