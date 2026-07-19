"""
    Que: Q4) Copy File Contents into Another File
        Problem Statement
        Write a program which accepts two file names from the user.
            First file is an existing file
            Second file is a new file
        Copy all contents from the first file into the second file.

        Input : ABC.txt
                Demo.txt

        Expected Output
        Contents of ABC.txt copied into Demo.txt.
"""

def main():
    FirstFile = input("Enter First File Name: ")
    SecondFile = input("Enter Second File Name: ")
    try:   
        fobj1 = open(FirstFile,"r")
        print("File gets opened")

        AllText = fobj1.read()

        fobj2 = open(SecondFile, "w")
        fobj2.write(AllText)

        print(f"Contents of {FirstFile} copied into {SecondFile}.")

        fobj1.close()
        fobj2.close()
        
        fobj2 = open(SecondFile, "r")
        print(f"Second file contains: {fobj2.read()}")

        fobj2.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()

"""
    Output is:
        Enter First File Name: Demo.txt
        Enter Second File Name: First.txt
        File gets opened
        Contents of Demo.txt copied into First.txt.
        Second file contains: Marvellous Infosystem
        Pune Pune
        Maharashtra
        India
"""