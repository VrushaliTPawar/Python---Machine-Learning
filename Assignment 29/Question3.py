"""
    Que: Q3) Copy File Contents into a New File (Command Line)
        Problem Statement
        Write a program which accepts an existing file name through command line arguments, 
        creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.

        Input (Command Line) : ABC.txt
        Expected Output
            Create Demo.txt and copy contents of ABC.txt into Demo.txt.
"""

import sys

def main():
    SourceFile = sys.argv[1]

    try:
        fobj1 = open(SourceFile, "r")
        Data = fobj1.read()

        fobj2 = open("Destination.txt", "w")
        fobj2.write(Data)

        print(f"Contents of {SourceFile} copied into Destination.txt")

        fobj2 = open("Destination.txt", "r")
        print(f"Contents of Destination.txt file \n{fobj2.read()}")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("Source file not found.")


if __name__ == "__main__":
    main()

"""
    Output is:
        Contents of Demo.txt copied into Destination.txt
        Contents of Destination.txt file
        Marvellous Infosystem
        Pune Pune
        Maharashtra
        India
"""