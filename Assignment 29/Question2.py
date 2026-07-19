"""
    Que: Q2) Display File Contents
        Problem Statement
        Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

        Input : Demo.txt 
        Expected Output
            Display contents of Demo.txt on console.
"""

import os
def main():
    FileName = input("Enter File Name: ")

    try:   
        fobj = open(FileName,"r")
        print("File gets opened")

        print(f"File Content \n{fobj.read()}")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()

"""
    Output is:
        Enter File Name: Demo.txt
        File does not exist.

        After Creating file Demo.txt
        Enter File Name: Demo.txt
        File Demo.txt exists.
"""