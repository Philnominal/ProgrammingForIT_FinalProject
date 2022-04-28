from tkinter import *
from tkinter import ttk
import random


def attributeGen():
    STR = random.randint(8, 18)
    DEX = random.randint(8, 18)
    CON = random.randint(8, 18)
    INT = random.randint(8, 18)
    WIS = random.randint(8, 18)
    CHA = random.randint(8, 18)
    attributes = STR, DEX, CON, INT, WIS, CHA
    return attributes

b = attributeGen()
print(b)
print(b[2])


#Settings for the initial window
window = Tk()
window.geometry('700x350')
window.title("Character Generation")
window.configure(bg="#f5d384")

#Creates the Name Label
lbl_charName = Label(window, text="Name:", bg="#e6bc5c",
                     borderwidth="1", relief="raised", font=("Ariel Bold", 15), width=10)
lbl_charName.grid(column=0, row=0, sticky='w')
#Creates the Entry box Next to Name Label
nameTxt = Entry(window, width=15)
nameTxt.grid(column=1, row=0)

#Creates the Gender Label
lbl_charGender = Label(window, text="Gender:", bg="#e6bc5c",
                     borderwidth="1", relief="raised", font=("Ariel Bold", 15), width=10)
lbl_charGender.grid(column=0, row=1, sticky='w')
#Creates the Entry box next to Gender Label
genderTxt = Entry(window, width=15)
genderTxt.grid(column=1, row=1)

#Creates the Character Background Label
lbl_charBackground = Label(window, text="Background:", bg="#e6bc5c",
                     borderwidth="1", relief="raised", font=("Ariel Bold", 14), width=10)
lbl_charBackground.grid(column=0, row=2)

#Creates the Entry box next to the Character Background Label
charBackgroundTxt = Entry(window, width=15)
charBackgroundTxt.grid(column=1, row =2)

#Creates the "Race" label
lbl_racialOption = Label(window, text="Race:", bg="#e6bc5c",
                     borderwidth="1", relief="raised", font=("Ariel Bold", 14), width=10)
lbl_racialOption.grid(column=0, row=3)
#Creates the combobox for the Race Label to choose race out of options
racialOption = ttk.Combobox(window, width=10)
racialOption.grid(column=1, row=3)
racialOption['values']=("Human", "Elf", "Dwarf", "Halfling", "Dragonborn")
racialOption.current(0)

#Creates Strength Label
lbl_STR = Label(window, text="Strength", relief ="raised", font=("Ariel Bold", 14), width=9,
                borderwidth="2", bg="#e6bc5c")
lbl_STR.grid(column=4, row=1)
#Creates the Label to show generated strength score
lbl_STRscore = Label(window, text=b[0], relief ="sunken", font=("Ariel Bold", 14), width=4,
                borderwidth="2", bg="white")
lbl_STRscore.grid(column=5, row=1)

#Creates the Dexterity lavel
lbl_DEX = Label(window, text="Dexterity", relief ="raised", font=("Ariel Bold", 14), width=9,
                borderwidth="2", bg="#e6bc5c")
lbl_DEX.grid(column=4, row=2)
#Creates the Label to show generated Dexterity score
lbl_DEXscore = Label(window, text=b[1], relief ="sunken", font=("Ariel Bold", 14), width=4,
                borderwidth="2", bg="white")
lbl_DEXscore.grid(column=5, row=2)

#Creates the Constitution Label
lbl_CON = Label(window, text="Constitution", relief ="raised", font=("Ariel Bold", 14), width=9,
                borderwidth="2", bg="#e6bc5c")
lbl_CON.grid(column=4, row=3)
#Creates the Label box to show generated Constitution score
lbl_CONscore = Label(window, text=b[2], relief ="sunken", font=("Ariel Bold", 14), width=4,
                borderwidth="2", bg="white")
lbl_CONscore.grid(column=5, row=3)

#Creates the Intelligence Label
lbl_INT = Label(window, text="Intelligence", relief ="raised", font=("Ariel Bold", 14), width=9,
                borderwidth="2", bg="#e6bc5c")
lbl_INT.grid(column=6, row=1)
#Creates the Label box to show generated Intelligence score
lbl_INTscore = Label(window, text=b[3], relief ="sunken", font=("Ariel Bold", 14), width=4,
                borderwidth="2", bg="white")
lbl_INTscore.grid(column=7, row=1)

#Creates the Wisdom Label
lbl_WIS = Label(window, text="Wisdom", relief ="raised", font=("Ariel Bold", 14), width=9,
                borderwidth="2", bg="#e6bc5c")
lbl_WIS.grid(column=6, row=2)
#Creates the Label box to show generated Wisdom score
lbl_WISscore = Label(window, text=b[4], relief ="sunken", font=("Ariel Bold", 14), width=4,
                borderwidth="2", bg="white")
lbl_WISscore.grid(column=7, row=2)

#Creates the Charisma Label
lbl_CHA = Label(window, text="Charisma", relief ="raised", font=("Ariel Bold", 14), width=9,
                borderwidth="2", bg="#e6bc5c")
lbl_CHA.grid(column=6, row=3)
#Creates the Label box to show generated Charisma score
lbl_CHAscore = Label(window, text=b[5], relief ="sunken", font=("Ariel Bold", 14), width=4,
                borderwidth="2", bg="white")
lbl_CHAscore.grid(column=7, row=3)

#Creates the Level Label
lbl_Level = Label(window, text="Level:", relief="raised", font=("Ariel Bold", 14), width=10,
               borderwidth="2", bg="#e6bc5c")
lbl_Level.grid(column=0, row=5)
#Creates the Level Dropdown box to choose level of character
levelOption = ttk.Combobox(window, width=2)
levelOption.grid(column=1, row=5)
levelOption['values']=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
levelOption.current(0)

#Creates the HP (Hit points) Label
lbl_HP = Label(window, text="HP:", relief="raised", font=("Ariel Bold", 14), width=10,
               borderwidth="2", bg="#e6bc5c")
lbl_HP.grid(column=0, row=6)
#Creates the Label to display the Max HP of the Character
lbl_HPscore = Label(window, text="PlaceH", relief ="sunken", font=("Ariel Bold", 12), width=6,
                borderwidth="2", bg="white")
lbl_HPscore.grid(column=1, row=6)

#Creates the Save File Button
saveFile_btn = Button(window, text="Save File", font=("Ariel Bold", 14), width=8,
                      borderwidth="2", bg="#e6bc5c")
saveFile_btn.grid(column=0, row=10)

#
printFile_btn = Button(window, text="Print", font=("Ariel Bold", 14), width=8,
                      borderwidth="2", bg="#e6bc5c")
printFile_btn.grid(column=0, row=11)

window.mainloop()