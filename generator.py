from tkinter import *
import random
from PIL import ImageTk, Image
from jobs import jobs, firstname, lastname
import json

with open('hobbies.json') as f:
    data = json.load(f)

with open('cities.json') as g:
    citydata = json.load(g)

def generate_new():
    global image_label
    global image
    global image_list

    random_int = random.randint(0, length_of_images - 2)
    #select a random image but excludes the last image in the list which is the profile picture

    random_color = random.choice(random_color_list)

    image_label.grid_forget()
    image_label = Label(image=image_list[random_int])
    image_label.grid(column=0, rowspan=2, row=3, columnspan=3, pady=30)
    root.config(bg=random_color)
    displayBio()
    cityCreated()
    #updates the character bio and updates the label

def formatImages():
    # Open images
    img_1 = Image.open("woman.jpg")
    img_1 = img_1.resize((150, 100), Image.ANTIALIAS)
    img_1 = ImageTk.PhotoImage(img_1)

    img_2 = Image.open("woman2.jpg")
    img_2 = img_2.resize((150, 100), Image.ANTIALIAS)
    img_2 = ImageTk.PhotoImage(img_2)

    img_3 = Image.open("woman3.jpg")
    img_3 = img_3.resize((150, 150), Image.ANTIALIAS)
    img_3 = ImageTk.PhotoImage(img_3)

    img_4 = Image.open("woman4.jpg")
    img_4 = img_4.resize((150, 100), Image.ANTIALIAS)
    img_4 = ImageTk.PhotoImage(img_4)

    img_5 = Image.open("woman5.jpg")
    img_5 = img_5.resize((100, 150), Image.ANTIALIAS)
    img_5 = ImageTk.PhotoImage(img_5)

    img_6 = Image.open("woman6.jpg")
    img_6 = img_6.resize((150, 100), Image.ANTIALIAS)
    img_6 = ImageTk.PhotoImage(img_6)

    img_7 = Image.open("woman7.jpg")
    img_7 = img_7.resize((100, 150), Image.ANTIALIAS)
    img_7 = ImageTk.PhotoImage(img_7)

    img_8 = Image.open("man1.jpg")
    img_8 = img_8.resize((100, 150), Image.ANTIALIAS)
    img_8 = ImageTk.PhotoImage(img_8)

    img_9 = Image.open("man2.jpg")
    img_9 = img_9.resize((100, 150), Image.ANTIALIAS)
    img_9 = ImageTk.PhotoImage(img_9)

    img_10 = Image.open("man3.jpg")
    img_10 = img_10.resize((150, 100), Image.ANTIALIAS)
    img_10 = ImageTk.PhotoImage(img_10)

    img_11 = Image.open("man4.jpg")
    img_11 = img_11.resize((100, 150), Image.ANTIALIAS)
    img_11 = ImageTk.PhotoImage(img_11)

    img_12 = Image.open("man5.jpg")
    img_12 = img_12.resize((100, 150), Image.ANTIALIAS)
    img_12 = ImageTk.PhotoImage(img_12)

    img_13 = Image.open("profile.jpg")
    img_13 = img_13.resize((150, 100), Image.ANTIALIAS)
    img_13 = ImageTk.PhotoImage(img_13)

    image_list = [img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8, img_9, img_10, img_11, img_12, img_13]
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
    city = cityCreated()
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
    #Creates 3 random hobbys

def cityCreated():
    rand_city_num = random.randint(0, len(citydata) - 1)
    character_city = citydata[rand_city_num]['city'] + ", " + citydata[rand_city_num]['state']
    return character_city
    #Creates a random location

root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title("Character Generator")

random_color_list = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    ]

global random_color
random_color = random.choice(random_color_list)
root.config(bg=random_color)


title = Label(root, text='Character Generator', font='arial 50 bold')
title.grid(column=0, row=0, rowspan=1)

image_list = formatImages()

global random_int
length_of_images = len(image_list)
random_int = random.randint(0, length_of_images - 1)

image_label = Label(root, image=image_list[-1], height=150, width=300, bg=random_color)
image_label.grid(column=0, rowspan=2, row=3, columnspan=3, pady=30, padx=40)

directions = 'Welcome to the Character Generator. '
directions2 = '\n Click "Generate New Character" to receive a fictional \n character name and biography.'

character_name_display = Label(root, text=directions, bg=random_color)
character_name_display.grid(column=0, row=5)
character_paragraph_display = Label(root, text=directions2, bg=random_color)
character_paragraph_display.grid(column=0, row=7, rowspan=4, pady=30)

new_character_btn = Button(root, text="Generate New Character", command=generate_new, bg="yellow")
new_character_btn.grid(column=0, row=11)

root.mainloop()