"""
    Que: Q1) Count Lines in a File
        Problem Statement
        Write a program which accepts a file name from the user and counts how many lines are present in the file.

        Input : Demo.txt
        Expected Output
        Total number of lines in Demo.txt
"""

def main():
    FileName = input("Enter File Name: ")
    try:   
        fobj = open(FileName,"r")
        print("File gets opened")

        count = 0
        for line in fobj:
            count = count + 1   
        print(f"Total number of lines in {FileName}: {count}")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()

"""
    Output is:
        Enter File Name: Demo.txt
        File gets opened
        Total number of lines in Demo.txt: 4
"""