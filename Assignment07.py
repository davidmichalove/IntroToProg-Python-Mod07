# ------------------------------------------------- #
# Title: <Type the name of the script here>
# Description: <Type a description of the script>
# ChangeLog: (Who, When, What)
# <David Michalove,05/30/2023,Created Script>
# ------------------------------------------------- #

# To Do:
# 1) Demonstrates: How PICKLING works
# 2) Demonstrates: How STRUCTURED ERROR HANDLING works

file_name_pickle = "pickleTest.dat" # Name of the data file
file_obj = None # An object representing a file
lst = []
import pickle
file_obj = open(file_name_pickle, "wb") # creates a binary file

print("Let's put some authors into a list.")
yesNo = "yes"
while yesNo.lower() == "yes":
    item = input("Please enter the name of an author: ")
    lst.append(item)
    yesNo = input("Do you want to enter another? [yes/no] ")
    while yesNo.lower() != "yes" and yesNo != "no":
        # Ensures the proper response from user
        print("Please only enter [yes/no] ")
        yesNo = input("Do you want to enter another? [yes/no] \n")

yesNo = input("Do you wish to save this list to your binary file? [yes/no] ")
while yesNo.lower() != "yes" and yesNo != "no":
    print("Please only enter [yes/no] ")
    yesNo = input("Do you wish to save this list to your binary file? [yes/no] \n")
if yesNo.lower() == "yes": # Saves items in lst into the binary file
    pickle.dump(lst, file_obj)
    file_obj.close()
else:
    print("OKAY")

yesNo = input("Do you wish to see what you've entered so far? [yes/no] ")
while yesNo.lower() != "yes" and yesNo != "no":
    print("Please only enter [yes/no] ")
    yesNo = input("Do you wish to see what you've entered so far? [yes/no] \n")
try:
    if yesNo.lower() == "yes": # Reads pickled objects
        file_obj = open(file_name_pickle, "rb")
        pickleLst = pickle.load(file_obj)
        print(pickleLst)
        file_obj.close()
    else:
        print("OKAY\n")
except EOFError and Exception as e:
    """Is raised when user forgot to save lst to binary file
       and when user wishes to read the empty file """
    print("You did not save your data.")
    print("Next time you need to save it before reading it.")
    print("Python would have told you:")
    print(e, e.__doc__, type(e), sep='\n')
    print("\n")

fileError = input("What other file would you like to open? ")
# Generates an error for the sake of practicing structured error handling
try:
    file_obj = open(file_name_pickle + fileError)
except IOError and Exception as e:
    print("That is not a file!")
    print("Python would have told you: ")
    print(e, e.__doc__, type(e), sep='\n') # Shows the python error message
    print("\n")
try:
    badSequence = input("Choose any number greater than " + str(len(lst)) + " ")
    print(lst[int(badSequence)])
except IndexError as e: # When index is out of range
    print("That is no proper index!")
    print("Python would have told you:")
    print(e, e.__doc__, type(e), sep='\n')
    print("\n")
except ValueError as e: # When a str is entered for an index position
    print("You'll need to give an integer and not a string.")
    print("Python would have told you:")
    print(e, e.__doc__, type(e), sep='\n')
    print("\n")
except Exception as e: # All other possible errors not accounted for
    print("That is no proper index!")
    print("Python would have told you:")
    print(e, e.__doc__, type(e), sep='\n')
    print("\n")

input("Enter any key to exit.")





