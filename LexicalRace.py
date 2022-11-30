########################
# TO-DO LIST           #
# solve path problem   #
# solve remove problem #
########################

# IMPORT LIBRARIES
import re
import urllib.request
from collections import Counter
from tkinter import *
import random

# function to set dictionary
def getWords(theme):

   
   theme = 'Football'
   URL = 'https://en.wikipedia.org/wiki/' + theme

   # get words from wikipedia page
   counter = Counter()
   with urllib.request.urlopen(URL) as source:
      for line in source:
         words = re.split(r"[^A-Z]+", line.decode('utf-8'), flags=re.I)
         counter.update(words)

   # get words from blank page 
   blankcounter = Counter()
   URL = 'https://en.wikipedia.org/wiki/Wikipedia:The_blank_page'
   with urllib.request.urlopen(URL) as source:
      for line in source:
         words = re.split(r"[^A-Z]+", line.decode('utf-8'), flags=re.I)
         blankcounter.update(words)

   # remove gibberish
   for key in blankcounter:
      if key in counter:
         del counter[key]
   
   listOfWords = list(counter.keys())
   return listOfWords

# function to add points to player and move horse
def point(player, horseList):

   # get horse position
   horse = horseList[player]
   print(list(horse.place_info()))
   (horsex, horsey) = horse.place_info()['x'], horse.place_info()['y']

   # update horse position
   horse.place(x = int(horsex) + 40, y = int(horsey))

# function to compare words and add points
def wordAssociation(wordlist, word, player, horseList):

   if word in wordlist:
      point(player-1, horseList)
      wordlist.pop(input)

# game itself
def lexicalRace(theme):

   # set up dictionary
   listOfWords=getWords(theme)

   # set up window
   window = Tk() # create window
   window.title("Lexical Race") # set title
   window.geometry("900x700") # set size
   font1 = ("Times", 24, "bold") # set font

   # position horses 
   horseList = []
   horse1image = PhotoImage(file = "/a-cavalo.png") # import image            ### COMPLETE WITH RIGHT PATH
   horse2image = PhotoImage(file = "/b-cavalo.png")                           ### COMPLETE WITH RIGHT PATH
   horse1 = Label(window, image = horse1image) # create label with image
   horse2 = Label(window, image = horse2image)
   horse1.place(x = 36, y = 233.3333333333333) # set position	
   horse2.place(x = 36, y = 466.66666666667)
   horseList.append(horse1) # create list with horses
   horseList.append(horse2)
   window.update() 

   # create user inputs
   horse1x = 36 # set position
   horse2x = 36
   userInput1 = Entry(window, width = 20, font=font1) # create text input
   userInput2 = Entry(window, width = 20, font=font1)
   userInput1.place(x = horse1x, y = 233 - 60) # set position
   userInput2.place(x = horse2x, y = 466 + 60)
   window.update()

   # create submit button for horse 1
   button1 = Button(window, text = "Submeter", font=font1, command= lambda: wordAssociation(listOfWords, userInput1.get(), 1, horseList)) # create button
   button1.place(x = 36, y = 233 - 120) # set position
   window.update()

   # create submit button for horse 2
   button2 = Button(window, text = "Submeter", font=font1, command= lambda: wordAssociation(listOfWords, userInput2.get(), 2, horseList)) # create button
   button2.place(x = 36, y = 466 + 120) # set position
   window.update()

   window.mainloop()

lexicalRace('Football')
