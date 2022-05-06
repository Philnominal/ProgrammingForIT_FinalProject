# ProgrammingForIT_FinalProject
#Name: Phillip D'Anjou
#Student ID: 00235395
#Assignment: Final Project
#Course: Programming for IT


Final Project for my Programming for IT course, a basic DnD character creation application.

Long Description:
  I am looking to create a DnD character creation application. This will generate a set of numbers to use as ability scores. You will then be able to assign them to specific attributes of STR, DEX, CON, INT, WIS, and CHA. You will input a name, choose a race, which will apply appropriate modifiers to the ability scores. You will then be able to save/and or print the created character to a document or printer. This will have a GUI to help facilitate all of this for the user. 
  
Resources Used:
  https://www.youtube.com/watch?v=VMP1oQOxfM0 - Helpful tutorial on Tkinter with great graphics!
  Class Demo Codes
  Class Weekly Materials/Learning Resources
  https://stackoverflow.com/questions/43170320/how-to-align-tkinter-widgets - Help aligning Tkinter widgets
  https://www.google.com/search?q=%23color+picker&oq=%23color&aqs=chrome.1.69i57j0i20i263i512j0i512j0i20i263i512j0i512l6.2767j0j9&sourceid=chrome&ie=UTF-8 - Generating color codes to use
  For help with mss module (Specifically for printing/Saving as .png to folder: https://python-mss.readthedocs.io/examples.html
  For help with binding multiple commands to the same button: https://www.geeksforgeeks.org/how-to-bind-multiple-commands-to-tkinter-button/
  General Help with Tkinter Usage - All of the many Tkinter tutorials from Codemy.com on youtube: https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

Completion Statement:
    Create a program that utilizes all of the main segments we discussed over the semester from class.
    Create a program based on the Long Description provided above.
   Challenges:
    -Figuring out how to fully utilize Tkinter functions.
    -Figuring out which modules were needed for the program and how to use them.
    -Figuring out how to combine multiple functions to work within a called button command functions.
    -Figuring out how to take a screenshot and then save it to a folder. 
     -Also how to have the user input what the name will be for both the .txt file and the .png file without using Input() for the terminal.
    -Using the attribute generation method to not only create the attributes, but to turn those into a dictionary and then return it as such.
    
Statement of Assistance:
  - The biggest help with this assignment was figuring out how to mix my codes with use of Tkinter. Codemy.com provided the most direct and helpful tutorials in doing so.
  - Class/Demo codes providing a base from which I started.
  - The professor, sitting down with me at the check-in portion and going over what was there and what was still needed.

Instructions - How to Operate:
  - Click run to start the code.
  - This will automatically generate the attribute scores and place them.
  - Enter your name, gender, and background in the listed entry boxes.
  - When done, click "Print/Save" and it will save and make two files based
      on what you entered for a name. A .txt file storing your originally generated ability scores
      and a .png file which a screenshot of your whole screen to access that specific sheet information for the future.
      
Application Dependencies:
  - from tkinter import *
  - from tkinter import ttk
  - import random
  - from mss import mss

Future Work:
  - If I had more time and knowdlege, in the future I would have liked to create a method of saving all the information as its own file to then click open/load for that specific saved file.
  - I would have liked to add a method of including a spot for a picture that could be uploaded by the user.
  - I would have added WAAAY more character gen information instead of just a basic setup.
