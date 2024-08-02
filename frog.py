from tkinter import *
from PIL import Image, ImageTk

class Frog:
    def __init__(self, x, y, width, height, speed=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        # Load and resize the image
        self.image = Image.open("frog.png")
        self.image = self.image.resize((self.width, self.height))
        self.tk_image = ImageTk.PhotoImage(self.image)

    def moveUp(self):
        self.y -= self.speed

    def moveLeft(self):
        self.x -= self.speed

    def moveRight(self):
        self.x += self.speed

    def paint(self, w):
        w.create_image(self.x, self.y, image=self.tk_image)

    def crashes(self,car):
        fx1,fy1=self.x,self.y
        fx2,fy2=self.x+self.width,self.y+self.height

        cx1,cy1=car.x,car.y  
        cx2,cy2=car.x+car.width,car.y+car.height

        if cx1<=fx1<=cx2 and cy1<=fy1<=cy2: #top left
            return True
        if cx1<=fx2<=cx2 and cy1<=fy1<=cy2: #top right
            return True
        if cx1<=fx2<=cx2 and cy1<=fy2<=cy2: #bottom right
            return True
        if cx1<=fx1<=cx2 and cy1<=fy2<=cy2: #bottom left
            return True
        return False
