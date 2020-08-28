from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from libs_image_filter import *

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

my_image = Image.open("./images/elephant.jpg")

filter_ascii(my_image, 1200, 1200)
# pixelated = filter_pixel("./images/elephant.jpg")


# img = ImageTk.PhotoImage(pixelated)
# canvas.create_image(20, 20, anchor=NW, image=img)
# root.mainloop()
