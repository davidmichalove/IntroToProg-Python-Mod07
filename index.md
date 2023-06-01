# Handling Jars 
*David Michalove, 5/30/2023*
*Course Name: IT FDN 110 A Sp 23: Foundations Of Programming: Python*
*Assignment: Assignment07*

## Introduction 
This paper is broken up into two main parts: Main, and The End Product. The Main section includes Pickling, Exception Handling, and the The Code Itself subsections. The End Product section includes PyCharm, Terminal, and pickleTest.dat. 

## Main 
### Pickling
The website article called pickle --- Python object serialization provides a great overview of the pickle module that gets into the specifics. Furthermore, this article is hosted on www.python.org., a reputable source for all things Python. A general example is: “the pickle module implements binary protocols for serializing and de-serializing a Python object structure.  “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.” (Pickle, https://docs.python.org/3/library/pickle.html#id7) (External Site)

A little further on, we can see the specifics of the pickle module develop: ““The pickle module can transform a complex object into a byte stream and it can transform the byte stream into an object with the same internal structure. Perhaps the most obvious thing to do with these byte streams is to write them onto a file, but it is also conceivable to send them across a network or store them in a database. The shelve module provides a simple interface to pickle and unpickle objects on DBM-style database files.” (Pickle, https://docs.python.org/3/library/pickle.html#id7) (External Site)

Furthermore, this article presents the functions related to pickling: its module interface. e.g., ““To serialize an object hierarchy, you simply call the dumps() function. Similarly, to de-serialize a data stream, you call the loads() function. However, if you want more control over serialization and de-serialization, you can create a Pickler or an Unpickler object, respectively.” 
Pickle, https://docs.python.org/3/library/pickle.html#id7) (External Site)

From these quotes we can see that “serialization” plays a main role in pickling. On the one hand, serialization seems to be the conversion from what is to be written into what is written into a binary file. On the other hand, de-serializing seems to be the conversion from what is written in a binary file into a language that the user can read. This process allows for much more complex information, pickled objects, to be stored in a fairly efficient and quick manner.

### Exception Handling
Exception handling seems to be a great way to make one’s program more secure while allowing for the user to have a better experience of it. Besides this, catching an error in this manor, will allow the program to continue onwards despite reaching an error. Without this technique it seems that when an error is hit upon then the program stops abruptly with an error code awaiting. It also seems that exception handling allows the user to learn what actions the code can accommodate and what the code cannot. From the side of a learning script writer, working with exception handling allows the standard error codes to become readable and brings clarification as to what they say, why they come up, and how they act as guides. Thinking about the many ways a code can fall apart or break through the actions of the user seems to bring with it a deeper sense to how the logic is being held together and the inner structures that allow the program to work smoothly. It seems that this way of approaching a piece of script enforces and promotes robustness. Again, the shift in tempo between exception handling and coding seems noticeably different. Both require a global tempo, and the specifics have different tempos. Exception handling seems to become relevant insofar as there is written script. But once incorporated quickly becomes part of the main script and its backbone. 

Here is a valuable website that goes into further details about exception handling: https://docs.python.org/3/tutorial/errors.html. This site is valuable as it sublimates the material in the course. Building on the general structures learned therein and expanding into specific areas. However, due to the details, it does not seem to be the best place to start if one has never encountered this topic before. On the other hand, this site shows how exception handling fits into a broader net and structure. In effect, situates it.

## The Code Itself 
-------------------------------------------------

Title: <Assignment07>

Description: <Type a description of the script>

ChangeLog: (Who, When, What)

<David Michalove,05/30/2023,Created Script>

-------------------------------------------------
To Do:
1) Demonstrates: How PICKLING works
2) Demonstrates: How STRUCTURED ERROR HANDLING works

file_name_pickle = "pickleTest.dat" """Name of the data file""" <br /> 
file_obj = None """An object representing a file""" <br /> 
lst = [] <br />
import pickle <br />
file_obj = open(file_name_pickle, "wb") # creates a binary file <br />
  
print("Let's put some authors into a list.") <br />
yesNo = "yes" <br />
while yesNo.lower() == "yes": <br />
&nbsp;&nbsp;&nbsp; item = input("Please enter the name of an author: ") <br />
&nbsp;&nbsp;&nbsp; lst.append(item) <br />
&nbsp;&nbsp;&nbsp; yesNo = input("Do you want to enter another? [yes/no] ") <br />
&nbsp;&nbsp;&nbsp; while yesNo.lower() != "yes" and yesNo != "no": <br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; # Ensures the proper response from user <br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; print("Please only enter [yes/no] ") <br />
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; yesNo = input("Do you want to enter another? [yes/no] \n") <br />

yesNo = input("Do you wish to save this list to your binary file? [yes/no] ") <br />
while yesNo.lower() != "yes" and yesNo != "no": <br />
&nbsp;&nbsp;&nbsp; print("Please only enter [yes/no] ") <br />
&nbsp;&nbsp;&nbsp; yesNo = input("Do you wish to save this list to your binary file? [yes/no] \n") <br />
if yesNo.lower() == "yes": # Saves items in lst into the binary file <br />
&nbsp;&nbsp;&nbsp; pickle.dump(lst, file_obj) <br />
&nbsp;&nbsp;&nbsp; file_obj.close() <br />
else: <br />
&nbsp;&nbsp;&nbsp; print("OKAY") <br />
yesNo = input("Do you wish to see what you've entered so far? [yes/no] ") <br />
while yesNo.lower() != "yes" and yesNo != "no": <br />
&nbsp;&nbsp;&nbsp; print("Please only enter [yes/no] ") <br />
&nbsp;&nbsp;&nbsp; yesNo = input("Do you wish to see what you've entered so far? [yes/no] \n") <br />
try: <br />
&nbsp;&nbsp;&nbsp; if yesNo.lower() == "yes": # Reads pickled objects <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; file_obj = open(file_name_pickle, "rb") <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pickleLst = pickle.load(file_obj) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print(pickleLst) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; file_obj.close() <br />
&nbsp;&nbsp;&nbsp; else: <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print("OKAY\n") <br />
except EOFError and Exception as e: <br />
&nbsp;&nbsp;&nbsp; """Is raised when user forgot to save lst to binary file <br />
&nbsp;&nbsp;&nbsp; and when user wishes to read the empty file """ <br />
&nbsp;&nbsp;&nbsp; print("You did not save your data.") <br />
&nbsp;&nbsp;&nbsp; print("Next time you need to save it before reading it.") <br />
&nbsp;&nbsp;&nbsp; print("Python would have told you:") <br />
&nbsp;&nbsp;&nbsp; print(e, e.__doc__, type(e), sep='\n') <br />
&nbsp;&nbsp;&nbsp; print("\n") <br />

fileError = input("What other file would you like to open? ") <br />
Generates an error for the sake of practicing structured error handling <br />
try: <br />
&nbsp;&nbsp;&nbsp; file_obj = open(file_name_pickle + fileError) <br />
except IOError and Exception as e: <br />
&nbsp;&nbsp;&nbsp; print("That is not a file!") <br />
&nbsp;&nbsp;&nbsp; print("Python would have told you: ") <br />
&nbsp;&nbsp;&nbsp; print(e, e.__doc__, type(e), sep='\n') # Shows the python error message <br />
&nbsp;&nbsp;&nbsp; print("\n") <br />
try: <br />
&nbsp;&nbsp;&nbsp; badSequence = input("Choose any number greater than " + str(len(lst)) + " ") <br />
&nbsp;&nbsp;&nbsp; print(lst[int(badSequence)]) <br />
except IndexError as e: # When index is out of range <br />
&nbsp;&nbsp;&nbsp; print("That is no proper index!") <br />
&nbsp;&nbsp;&nbsp; print("Python would have told you:") <br />
&nbsp;&nbsp;&nbsp; print(e, e.__doc__, type(e), sep='\n') <br />
&nbsp;&nbsp;&nbsp; print("\n") <br />
except ValueError as e: # When a str is entered for an index position <br />
&nbsp;&nbsp;&nbsp; print("You'll need to give an integer and not a string.") <br />
&nbsp;&nbsp;&nbsp; print("Python would have told you:") <br />
&nbsp;&nbsp;&nbsp; print(e, e.__doc__, type(e), sep='\n') <br />
&nbsp;&nbsp;&nbsp; print("\n") <br />
except Exception as e: # All other possible errors not accounted for <br />
&nbsp;&nbsp;&nbsp; print("That is no proper index!") <br />
&nbsp;&nbsp;&nbsp; print("Python would have told you:") <br />
&nbsp;&nbsp;&nbsp; print(e, e.__doc__, type(e), sep='\n') <br />
&nbsp;&nbsp;&nbsp; print("\n") <br />

input("Enter any key to exit.") <br />
  
## The End Product <br />
### PyCharm<br />
<img width="448" alt="Screenshot 2023-06-01 at 2 21 23 AM" src="https://github.com/davidmichalove/IntroToProg-Python-Mod07/assets/133909395/faf8b7f5-5bd1-4c99-8be3-5361ad3155d2">

### Terminal <br />
<img width="633" alt="Screenshot 2023-06-01 at 2 24 17 AM" src="https://github.com/davidmichalove/IntroToProg-Python-Mod07/assets/133909395/5a1fab23-89f0-43b0-aaa4-5f564a3aa6ac">

## Summary<br />
There were two main parts in this paper: Main, and The End Product. The Main section sheltered Pickling, Exception Handling, and the The Code Itself subsections. The End Product was made up by PyCharm, Terminal, and pickleTest.dat subsections. <br />
