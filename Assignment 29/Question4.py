"""
    Que: Q4) Compare Two Files (Command Line)
        Problem Statement
        Write a program which accepts two file names through command line arguments and compares the contents of both files.
            If both files contain the same contents, display Success
            Otherwise display Failure

        Input (Command Line) : Demo.txt Hello.txt
        Expected Output
            Success OR Failure
"""

import sys

def main():
    try:
        FirstFile = sys.argv[1]
        SecondFile = sys.argv[2]

        fobj1 = open(FirstFile, "r")
        fobj2 = open(SecondFile, "r")

        Data1 = fobj1.read()
        Data2 = fobj2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("File not found.")

    except IndexError:
        print("Usage: python program.py <FirstFile> <SecondFile>")


if __name__ == "__main__":
    main()

"""
    Output is:
        python Question4.py Demo.txt Destination.txt
        Success
"""