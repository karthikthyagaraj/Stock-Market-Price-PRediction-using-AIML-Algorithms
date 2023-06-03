import os
from tkinter import *

# create the main window
root = Tk()
root.title('Login Page')

# get the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the frame size based on the screen size
frame_width = int(screen_width * 0.3)
frame_height = int(screen_height * 0.3)

# center the frame on the screen
x = int((screen_width - frame_width) / 2)
y = int((screen_height - frame_height) / 2)
root.geometry(f'{frame_width}x{frame_height}+{x}+{y}')

# create labels for the username and password fields
username_label = Label(root, text='Username:')
password_label = Label(root, text='Password:')

# create entry widgets for the username and password fields
username_entry = Entry(root)
password_entry = Entry(root, show='*')  

username_label.grid(row=0, column=0, pady=5, sticky='e')
password_label.grid(row=1, column=0, pady=5, sticky='e')
username_entry.grid(row=0, column=1, pady=5, padx=5, sticky='w')
password_entry.grid(row=1, column=1, pady=5, padx=5, sticky='w')

# define a function to check if the login credentials are valid
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == 'admin' and password == 'password123':
        print('Login successful!')
        os.system('python FINAL_UI.py')  
    else:
        print('Invalid username or password')

# create a login button that calls the login function when clicked
login_button = Button(root, text='Login', command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# center the label and entry widgets
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# start the main loop to display the window
root.mainloop()
