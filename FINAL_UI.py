from tkinter import *
import numpy as np
import pandas as pd
import os
import tkinter as tk
import PIL
from tkinter import ttk
from PIL import ImageTk, Image  

app = Tk()
app.title("Welcome")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}")

# Add images
image_list = ["background1.jpg", "background5.jpg", "background3.jpg", "background2.jpg", "background4.jpg"]
bg_images = []
for image in image_list:
    img = Image.open(image)
    img = img.resize((screen_width, screen_height))
    bg_images.append(ImageTk.PhotoImage(img))

# Define function to update background image
def update_bg(counter):
    label.config(image=bg_images[counter])
    app.after(2500, update_bg, (counter+1)%len(bg_images))

# Add initial background image
label = Label(app, image=bg_images[0])
label.place(x=0, y=0)

# Call update_bg function to change background image every 3 seconds
app.after(3000, update_bg, 1)

# Add text
label2 = Label(app, text="STOCKS AND CRYPTO PRICE PREDICTION \n USING ARIMA STATSMODELS",
               font=("Times", 24, "bold underline"), fg="#008080")
label2.place(x=screen_width//3-10, y=95)
label2 = Label(app, text="Choose Model to predict the flow of prize",
               font=("Times", 20, "bold "), fg="#008080")
label2.place(x=screen_width//2-200, y=200)

def ardat():
    os.system('python AR.py')

def ari():
    os.system('python ARIMA.py')

def bay():
    os.system('python bayesian.py')

def pol():
    os.system('python var.py')

def sar():
    os.system('python SARIMAX.py')

def auar():
    os.system('python auto-ARIMA.py')

# Update buttons with more space between them and a modern look
button_style = ttk.Style()
button_style.configure('TButton', font=('calibri', 20, 'bold'), foreground='#008080', background='#071329', width=20, anchor=CENTER)

pms = ttk.Button(app, text="AR", command=ardat, style='TButton')
pms.place(x=screen_width//4-100, y=350)

sb = ttk.Button(app, text="ARIMA", command=ari, style='TButton')
sb.place(x=screen_width//4-100, y=450)

pms = ttk.Button(app, text="BAYSEAN", command=bay, style='TButton')
pms.place(x=screen_width//4-100, y=550)

sb = ttk.Button(app, text="VAR", command=pol, style='TButton')
sb.place(x=3*screen_width//4-100, y=350)

pms = ttk.Button(app, text="SARIMAX", command=sar, style='TButton')
pms.place(x=3*screen_width//4-100, y=450)

sb = ttk.Button(app, text="AUTO-ARIMA", command=auar, style='TButton')
sb.place(x=3*screen_width//4-100, y=550)

# Execute tkinter
app.mainloop()
