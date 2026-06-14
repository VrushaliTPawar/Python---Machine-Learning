"""
    Que: What is the purpose of getsizeof()?
    Why is memory size different for different data type?
"""

"""
    Answer:
    -> The getsizeof() function returns the memory size (in bytes) occupies by an object.
    -> Different data types need different amounts of memory because they store different kinds and amounts of information.
"""

num1 = 10
# print(getsizeof(num1)) -> Error because we need to import sys module.

"""
    Correct code:
    import sys

    num1 = 10
    print(sys.getsizeof(num1))
"""