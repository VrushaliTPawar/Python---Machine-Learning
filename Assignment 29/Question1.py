"""
    Que: Q1) Check File Exists in Current Directory
        Problem Statement
        Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

        Input : Demo.txt
        Expected Output
        Display whether Demo.txt exists or not.
"""

import os
def main():
    FileName = input("Enter File Name: ")
    if os.path.exists(FileName):
        print(f"File {FileName} exists.")
    else:
        print("File does not exist.")


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