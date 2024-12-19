import requests
from tkinter import filedialog, Tk, Menu, Listbox, Button, Frame, PhotoImage, END
import pygame
import os

def download_image(image_url,file_name):
    response = requests.get(image_url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

download_image('https://media.geeksforgeeks.org/wp-content/uploads/20240610151925/background.png','background.png')

app = Tk()
app.title('Test1')
app.geometry("100000x10000000")

app_icon = PhotoImage(file='background.png')
app.iconphoto(False, app_icon)

pygame.mixer.init()

menu_bar = Menu(app)
app.config(menu=menu_bar)

app.mainloop()