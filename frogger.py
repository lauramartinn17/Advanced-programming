from tkinter import *
import time
from tkinter import messagebox
import keyboard  # To install, type: py -m pip install keyboard
from frogger_constants import *
from car import *
from frog import Frog
from PIL import Image, ImageTk

# Inicializar la ventana principal y el canvas
tk = Tk() #Crear la ventana principal
w = Canvas(tk, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
w.pack()# Agregamos canvas a la ventana principal

class Lane:
    def __init__(self, num_of_cars, y, speed, height=50, carsColor="red", carsWidth=50):
        self.height = height
        self.y = y
        y_offset = (height - 30) / 2  # centrar los coches verticalmente en el carril
        cars_space = (carsWidth - 10) * 2 # Espacio entre coches
        self.cars = []
        for i in range(num_of_cars):
            car = Car(50 + cars_space * i, y + y_offset, carsWidth, 30, speed, carsColor) #Crear un coche
            self.cars.append(car)

    def moveCars(self):
        for c in self.cars:
            c.move() # Movimento de cada coche en el carril

    def paint(self, w):
        w.create_rectangle(0, self.y, SCREEN_WIDTH, self.y + self.height, fill="grey")
        for c in self.cars:
            c.paint(w) # Pintar cada coche en el carril

# Inicializar carriles y rana 
lanes = [
    Lane(5, 50, 1, carsColor="blue"),
    Lane(3, 100, -10, carsColor="green", carsWidth=100),
    Lane(5, 150, 5)
]
frog = Frog(400, 500, 30, 30, speed=10) # Inicializar la rana en la posición de inicio
t0 = time.time() # Registrar el tiempo de inicio
game_paused = False # Seguimiento del estado del juego (pausado o no)
game_won = False # Seguimiento del estado del juego (ganado o no)

def display_score():
    global game_paused
    current_time = round(time.time() - t0, 2) # Calculamos el tiempo transcurrido
    score = 100 - current_time # Calculamos puntuacion 100 - tiempo transcurrido
    messagebox.showinfo("YOU WON!!!", f"Score: {score:.2f}") # Mostrar puntuacion en una ventana emergente
    game_paused = True # Como hemos ganado pausamos el juego
    tk.destroy() # Cerramos el juego al aceptar o cerrar el mensaje emergente

def show_pause_message():
    global game_paused
    if game_paused:
        messagebox.showinfo("Game Paused", "The game is paused. Press 'Aceptar' to continue.") # Mensaje de pausa
        game_paused = False  # Continuar con el juego al cerrar el mensaje

while True:

    if not game_paused:
        w.delete("all")
        cur_time = round(time.time() - t0, 2) # Calcular el tiempo actual

        if keyboard.is_pressed("up arrow"):
            frog.moveUp()
        if keyboard.is_pressed("left arrow"):
            frog.moveLeft()
        if keyboard.is_pressed("right arrow"):
            frog.moveRight()
        if keyboard.is_pressed("p"): # Verificar si se presionó 'p' para pausar el juego
            if not game_paused:
                game_paused = True
                show_pause_message()
        for lane in lanes:
            lane.moveCars() # Mover los coches en cada carril

        for lane in lanes:
            for car in lane.cars:
                if frog.crashes(car):  # Verificar si la rana choca con algún coche
                    frog.x, frog.y = 400, 500 # Si choca restablecemos la posición de la rana
                    messagebox.showinfo(" ", "CRASHHHHH!!!!")

        if frog.y <= 10 and not game_won: # Verificar si la rana llega a la parte superior de la pantalla
            game_won = True
            display_score() # Mostrar la puntuacón

        for lane in lanes:
            lane.paint(w) # Pintar cada carril
        frog.paint(w) # Pintar el sapo
        w.create_text(700, 20, text=f"time: {cur_time:.2f}") # Mostrar el tiempo 
        w.update() # Actualizar el lienzo
        time.sleep(50 / 1000)  # 50ms delay
    else:
        time.sleep(50 / 1000)

tk.mainloop()
