from tkinter import *
import random
from PIL import ImageTk, Image

def generate_new():
    character_name = "ihiin"
    print(character_name)
    return character_name


root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title("Character Generator")
root.config(bg='red')

title = Label(root, text='Character Generator', font='arial 50 bold')
title.grid(column=0, row=0, rowspan=1)


image = Image.open("woman.jpg")
image = image.resize((150, 100), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
# Resizes the image on the screen

image_label = Label(root, image=image, height=100, width=150, bg="red")
image_label.grid(column=0, rowspan=2, row=3, columnspan=3, pady=30)

character_name = StringVar()
character_name = "Test"
character_paragraph = "Paragraph"

character_name_display = Label(root, text=character_name, bg="red")
character_name_display.grid(column=0, row=5)
character_paragraph_display = Label(root, text=character_paragraph, bg="red")
character_paragraph_display.grid(column=0, row=7, rowspan=4, pady=30)

new_character_btn = Button(root, text="Generate New Character", command=generate_new)
new_character_btn.grid(column=0, row=11)

root.mainloop()

