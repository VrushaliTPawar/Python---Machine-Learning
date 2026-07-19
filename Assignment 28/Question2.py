"""
    Que: Q2) Count Words in a File
        Problem Statement
        Write a program which accepts a file name from the user and counts the total number of words in that file.

        Input : Demo.txt
        Expected Output
        Total number of words in Demo.txt.
"""

def main():
    FileName = input("Enter File Name: ")
    try:   
        fobj = open(FileName,"r")
        print("File gets opened")

        text = fobj.read()
        words = text.split()

        print(f"Total number of words in {FileName}: {len(words)}")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()

"""
    Output is:
        Enter File Name: Demo.txt
        File gets opened
        Total number of words in Demo.txt: 5

    Other way :
        count = 0

        for line in file:
            words = line.split()      # Split line into words
            count += len(words)       # Add number of words
"""