"""
    Que: What is the difference between:
        a = 10
        b = 10
    and 
        a = [10]
        b = [10]
    Explain using id().
"""

a = 10
print(id(a))    # 140718547518872
b = 10
print(id(b))    # 140718547518872

a = [10]
print(id(a))    # 1975627593856
b = [10]
print(id(b))    # 1975627477312

"""
    Answer: 
        Basic : Python may reuses immutable objects, but it creates new mutable objects.
        Case 1: Integer
                a = 10
                b = 10
            10 is immutable. Nobody can change the integer object 10. 
            So instead of creating a new object every time it sees 10, Python reuses the existing object.
            So Python can safely do:
                a ──┐
                    ▼
                    10
                    ▲
                b ──┘
            Now even if a = 20
            Python doesn't modify 10; it simply makes a point to another integer object.

        Case 2: List
            Lists are mutable objects.
            Each list literal ([10]) creates a new list object in memory.
                a ──► [10]
                b ──► [10]
            Now what if a.append(20)
            then a becomes [10, 20]
            print(b) -> [10, 20] even though you never modified b.
            Therefore Python creates two separate list objects

"""