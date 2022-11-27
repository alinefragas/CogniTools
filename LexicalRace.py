import re
import urllib.request
from collections import Counter

theme = 'Football'
URL = 'https://en.wikipedia.org/wiki/' + theme


counter = Counter()
with urllib.request.urlopen(URL) as source:
    for line in source:
        words = re.split(r"[^A-Z]+", line.decode('utf-8'), flags=re.I)
        counter.update(words)

blankcounter = Counter()
URL = 'https://en.wikipedia.org/wiki/Wikipedia:The_blank_page'
with urllib.request.urlopen(URL) as source:
    for line in source:
        words = re.split(r"[^A-Z]+", line.decode('utf-8'), flags=re.I)
        blankcounter.update(words)


#remove keys from sea that are in emptyPage
for key in blankcounter:
    if key in counter:
        del counter[key]

listOfWords = list(counter.keys())
print(listOfWords)

#Start a python GUI
#Import the tkinter module
from tkinter import *
import random
window = Tk()
window.title("Lexical Race")
window.geometry("900x700")
#tkinter bigger font
font1 = ("Times", 24, "bold")

#Create a image


horse2image = PhotoImage(file = "/Users/alinegouveia/Documents/GitHub/CogniTools/CogniTools/b-cavalo.png")
horse2 = Label(window, image = horse2image)
horse2.place(x = 36, y = 233.3333333333333)	
window.update()

horse1image = PhotoImage(file = "/Users/alinegouveia/Documents/GitHub/CogniTools/CogniTools/a-cavalo.png")
horse1 = Label(window, image = horse1image)
horse1.place(x = 36, y = 466.66666666667)	
window.update()

def point(player):
    if player == 1:
        global horse1x
        horse1x = horse1x + 40
        horse1.place(x = horse1x, y = 466.3333333333333)
        window.update()

    if player == 2:
        global horse2x
        horse2x = horse2x + 40
        horse2.place(x = horse2x, y = 233.66666666667)
        window.update()


def wordAssociation(player):
    #see if the input is in the list of words
    input=userInput1.get()

    if input in listOfWords:
        print("Correct")
        #remove the word from the list
        listOfWords.remove(input)
        point(player)
    else:
        window.bell()


#create user input
horse1x = 36
userInput1 = Entry(window, width = 20, font=font1)
userInput1.place(x = horse1x, y = 233 - 60)
window.update()
#create button to submit user input
button1 = Button(window, text = "Submeter", font=font1, command= wordAssociation(1))
button1.place(x = 36, y = 233 - 120)
window.update()

horse2x = 36
userInput2 = Entry(window, width = 20, font=font1)
userInput2.place(x = horse2x, y = 466 + 70)
window.update()


        


window.mainloop()
