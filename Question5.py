"""
    Que: Q5) Search a Word in File
        Problem Statement
        Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

        Input : Demo.txt Marvellous
        Expected Output
            Display whether the word Marvellous is found in Demo.txt or not.
"""

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
        Enter the word :Pune
        File gets opened
        Word :  Pune
        Word :  Pune
        UserWord Pune occurred 2 times.

        Enter File Name: Demo.txt
        Enter the word : Marvellous
        File gets opened
        Word :  Marvellous
        UserWord Marvellous occurred 1 times.

        Enter File Name: Demo.txt
        Enter the word : pune
        File gets opened
        UserWord pune occurred 0 times.
"""