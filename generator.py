from tkinter import *
import random
from PIL import ImageTk, Image


def generate_new():
    global image_label
    global image
    global image_list

    random_int = random.randint(0, length_of_images - 1)

    image_label.grid_forget()
    image_label = Label(image=image_list[random_int])
    image_label.grid(column=0, rowspan=2, row=3, columnspan=3, pady=30)
    character_name_display['text'] = "ty"
    character_paragraph_display['text'] = "new paragraph"

def formatImages():
    # Open images
    img_1 = Image.open("woman.jpg")
    img_1 = img_1.resize((150, 100), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img_1)

    img_2 = Image.open("image1.jpg")
    img_2 = img_2.resize((150, 100), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img_2)

    img_3 = Image.open("woman2.jpg")
    img_3 = img_3.resize((150, 100), Image.ANTIALIAS)
    img_3 = ImageTk.PhotoImage(img_3)

    image_list = [img_1, img_2, img_3]
    return image_list

root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title("Character Generator")
root.config(bg='red')

title = Label(root, text='Character Generator', font='arial 50 bold')
title.grid(column=0, row=0, rowspan=1)

image_list = formatImages()

global random_int
length_of_images = len(image_list)
random_int = random.randint(0, length_of_images - 1)
print(length_of_images)

image_label = Label(root, image=image_list[2], height=100, width=150, bg="red")
image_label.grid(column=0, rowspan=2, row=3, columnspan=3, pady=30)




character_name = StringVar()
first_name = "Susan"
last_name = "Attwater"
career = "doctor"
city = "Chicago"
character_name = "Your character's name is " + first_name + " " +last_name
character_paragraph = first_name + " is a " + career + " from " + city + "."

character_name_display = Label(root, text=character_name, bg="red")
character_name_display.grid(column=0, row=5)
character_paragraph_display = Label(root, text=character_paragraph, bg="red")
character_paragraph_display.grid(column=0, row=7, rowspan=4, pady=30)

new_character_btn = Button(root, text="Generate New Character", command=generate_new)
new_character_btn.grid(column=0, row=11)

root.mainloop()