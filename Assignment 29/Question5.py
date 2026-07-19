"""
    Que: Q5) Frequency of a String in File
        Problem Statement
        Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

        Input : Demo.txt
                Marvellous
        Expected Output
            Count how many times "Marvellous" appears in Demo.txt.
"""

import sys

def main():
    FileName = input("Enter File Name: ")
    UserWord = input("Enter the word : ")
    try:   
        fobj = open(FileName,"r")
        print("File gets opened")

        AllText = fobj.read()
        AllWords = AllText.split()

        WordCount = 0   
        for w in AllWords:
            if w == UserWord:
                print("Word : ",w)
                WordCount = WordCount + 1

        print(f"UserWord {UserWord} occurred {WordCount} times.")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()

"""
    Output is:
        Enter File Name: Demo.txt
        Enter the word : Pune
        File gets opened
        Word :  Pune
        Word :  Pune
        UserWord Pune occurred 2 times.
"""