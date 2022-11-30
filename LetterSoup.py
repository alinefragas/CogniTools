#Start a python GUI
#Import the tkinter module
from tkinter import *
import random
window = Tk()
window.title("Letter Soup")
window.geometry("900x700")
#tkinter bigger font
font1 = ("Times", 24, "bold")
#Create a label

target = 0
window.configure(background='white')

#Create a label
palavra = "FAringe"
#convert to upper case
palavra = palavra.upper()

#Place the word on top
label = Label(window, text = palavra, font=font1)

#break a string into a list of strings with each word as an item

letters = list(palavra)
print(letters)
listButtons = []

listX= random.sample(range(50,850), len(letters))
for i,letter in enumerate(letters):
    x = listX[i]
    print(i)
    y = random.randint(50, 650)

   
    listButtons.append( Button(window, text = str(letter), font=font1, command= lambda w= i :onClick(w)))
    listButtons[i].place(x = x, y = y)
    window.update()
    

print(listButtons)
#delete button from screen

def onClick(i):
    global target
    if i == target:
       
        print(letters[i])
        listButtons[i].destroy()
        target = target + 1
    else:
        #play sound in tkinter
        print("wrong")
        window.bell()


#Display the label
label.pack()
#Start the event loop

#create a button that disapears if you click it
button = Button(window, text = "Click Me", command = Button.destroy)
button.pack()


window.mainloop()