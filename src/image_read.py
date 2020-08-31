from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from libs_image_filter import *

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()


# pixelated = filter_pixel("../tools/images/tiger.jpg")
filter_ascii("../tools/images/elephant.jpg", 1200, 1200)


# img = ImageTk.PhotoImage(pixelated)
# canvas.create_image(20, 20, anchor=NW, image=img)
# root.mainloop()
