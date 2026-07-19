"""
    Que: Q3) Count Frequency of a Particular String in a File
        Problem Statement
        Write a program which accepts a file name and one string from the user. Count how many times that string occurs in the file.
        
        Input : Demo.txt

        Expected Output
        Display each line of Demo.txt.
"""

def main():
    FileName = input("Enter File Name: ")
    UserWord = input("Enter the word :")
    try:   
        fobj = open(FileName,"r")
        print("File gets opened")

        AllText = fobj.read()
        AllWords = AllText.split()

        WordCount = 0
        for w in AllWords:
            if w == UserWord:
                WordCount = WordCount + 1

        print(f"String occurred {WordCount} times.")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()

"""
    Output is:
        Enter File Name: Demo.txt
        Enter the word :Pune
        File gets opened
        String occurred 1 times.

        After adding one more time Pune word
        D:\Python Machine Learning\Assignments\Assignment 28>python Question3.py
        Enter File Name: Demo.txt
        Enter the word :Pune
        File gets opened
        String occurred 2 times.
"""