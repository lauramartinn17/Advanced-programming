from frogger_constants import *
class Car:
    def __init__(self,x,y,width,height,speed=1,color="red") :
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.speed=speed
        self.color=color
    def move(self):
        self.x=self.x+self.speed
        if self.x>SCREEN_WIDTH and self.speed>0:
            self.x=0-self.width
        if self.x<0 and self.speed<0:
            self.x=SCREEN_WIDTH
    def paint(self,w):
        w.create_rectangle(self.x,self.y,
                           self.x+self.width,
                           self.y+self.height,fill=self.color)
        if self.speed>0:
            w.create_line(self.x+self.width*0.75,self.y,
                      self.x+self.width*0.75,self.y+self.height)
        else:
            w.create_line(self.x+self.width*0.25,self.y,
                      self.x+self.width*0.25,self.y+self.height)