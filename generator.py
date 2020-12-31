from tkinter import *
import random
from PIL import ImageTk, Image
from jobs import jobs, firstname, lastname
import json

with open('hobbies.json') as f:
    data = json.load(f)


def generate_new():
    global image_label
    global image
    global image_list

    random_int = random.randint(0, length_of_images - 1)

    image_label.grid_forget()
    image_label = Label(image=image_list[random_int])
    image_label.grid(column=0, rowspan=2, row=3, columnspan=3, pady=30)
    root.config(bg=random_color)
    displayBio()


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

def displayBio():
    global character_name_display
    global character_paragraph_display
    global first_name
    global last_name
    global career
    global character_name
    global character_paragraph
    global city
    global hobbies

    character_name_display.grid_forget()
    character_paragraph_display.grid_forget()

    first_name = random.choice(firstname)
    last_name = random.choice(lastname)
    career = random.choice(jobs)
    city = "St Louis"
    hobbies = hobbyCreate()

    character_name = "Your character's name is " + first_name + " " + last_name
    character_paragraph = first_name + " is a " + career + " from " + city + "." + hobbies

    character_name_display = Label(text=character_name)
    character_paragraph_display = Label(text=character_paragraph)
    character_name_display.grid(column=0, row=5)
    character_paragraph_display.grid(column=0, row=7, rowspan=4, pady=30)

def hobbyCreate():
    global hobby1
    global hobby2
    global hobby3
    rand1 = random.randint(0, len(data) - 1)
    rand2 = random.randint(0, len(data) - 1)
    rand3 = random.randint(0, len(data) - 1)
    hobby1 = data[rand1]["title"]
    hobby2 = data[rand2]["title"]
    hobby3 = data[rand3]["title"]
    returned_hobby = "\n \nThis person's interests include: \n" + hobby1.lower() + ", " + hobby2.lower() + ", and \n" + hobby3.lower() + "."
    return returned_hobby
root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title("Character Generator")
global random_color
random_color = "red"
root.config(bg=random_color)


title = Label(root, text='Character Generator', font='arial 50 bold')
title.grid(column=0, row=0, rowspan=1)

image_list = formatImages()

global random_int
length_of_images = len(image_list)
random_int = random.randint(0, length_of_images - 1)

image_label = Label(root, image=image_list[2], height=100, width=150, bg=random_color)
image_label.grid(column=0, rowspan=2, row=3, columnspan=3, pady=30)

character_name = StringVar()
first_name = random.choice(firstname)
last_name = random.choice(lastname)
career = random.choice(jobs)
city = "Chicago"

global hobby1
global hobby2
global hobby3

hobbies = hobbyCreate()
character_name = "Your character's name is " + first_name + " " + last_name
character_paragraph = first_name + " is a " + career + " from " + city + "." + hobbies

directions = 'Welcome to the Character Generator. \n Click "Generate New Character" to receive a fictional \n character name and biography'
directions2 = ""

character_name_display = Label(root, text=directions, bg=random_color)
character_name_display.grid(column=0, row=5)
character_paragraph_display = Label(root, text=directions2, bg=random_color)
character_paragraph_display.grid(column=0, row=7, rowspan=4, pady=30)

new_character_btn = Button(root, text="Generate New Character", command=generate_new)
new_character_btn.grid(column=0, row=11)

root.mainloop()