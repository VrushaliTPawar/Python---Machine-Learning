"""
    Que:
        Write a program to take user's name and age and display:
        Hello <name>, you will turn <age+1> next year.
"""


print("Enter your name :")
name = input()

print("Enter your age :")
age = int(input())

print("Hello " + name + ", you will turn " + str(age + 1) + " next year.")


print(f"Hello {name}, you will turn {age + 1} next year.")      # recommended
print("Hello {}, you will turn {} next year.".format(name, age + 1))
print("Hello {n}, you will turn {a} next year.".format(n=name, a=age+1))
print("Hello %s, you will turn %d next year." % (name, age + 1))
print("Hello", name + ",", "you will turn", age + 1, "next year.")