"""
    Que: What does the id() function return?
    Is the value returned by id() same for two variable holding the same value?
"""

num1 = 10
print(id(num1))    # 140718547518872
num2 = 10
print(id(num2))    # 140718547518872

"""
    Answer :
    -> The id() funtion returns the unique identity (memory address) of an object.
    -> Yes, its same for two variable holding the same value because python reuses immutable objects.
"""