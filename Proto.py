#Librerias
import tkinter as tk
from PIL import ImageTk, Image
import pygame
import random
import time
from threading import Thread

#Puntuacion
global score
score = 0
jump_counter = 0

#SplashAnimation (Se usaron las idead presentadas por Codemy.com, de generar el splash por medio de una ventana)
anim = tk.Tk()
anim.geometry("1080x720")
anim.geometry("+250+50")
anim.overrideredirect(True)
anim.configure(background="black")
titulo1 = tk.Label(anim, text= "The Monkey is the key...but he is also death...a herald of doom...", font= "Papyrus", bg= "black",
                   fg= "white")
titulo1.pack(pady=20)
titulo2 = tk.Label(anim, text= "...can you KILL him...he is no longer a monkey, for he is the DEMON MONKEY!",
                   font= "Papyrus", bg= "black", fg= "white")
titulo2.pack(pady=25)
titulo3 = tk.Label(anim, text= "Monkey: Tears and Blood", font= ("Papyrus", 40), bg= "black", fg= "white")
titulo3.pack(pady=40)
titulo4 = tk.Label(anim, text= "Developed by Esteban Secaida", font= ("Papyrus", 40), bg= "black", fg= "white")
titulo4.pack(pady=50)
titulo5 = tk.Label(anim, text= "A not that bad-looking young man that loves to eat", font= ("Papyrus", 15), bg= "black", fg= "white")
titulo5.pack(pady=40)
imageYocanvas = tk.Canvas(anim, width=200, height=446, borderwidth=0, highlightthickness=0, bg="white")
imageYocanvas.place(x=850, y=500)
imageYo = Image.open("yo.png")
resizedYo = imageYo.resize((225, 300), Image.ANTIALIAS)
nuevoYo = ImageTk.PhotoImage(resizedYo, master=imageYocanvas)
imageYocanvas.create_image(215, 100, image=nuevoYo, anchor=tk.E)
imageHcanvas = tk.Canvas(anim, width=200, height=446, borderwidth=0, highlightthickness=0, bg="white")
imageHcanvas.place(x=75, y=500)
imageH = Image.open("harambe.png")
resizedH = imageH.resize((225, 300), Image.ANTIALIAS)
nuevoH = ImageTk.PhotoImage(resizedH, master=imageHcanvas)
imageHcanvas.create_image(215, 100, image=nuevoH, anchor=tk.E)

#Ventana de Menu
def main():
    anim.destroy()
    menuwindow = tk.Tk()
    menuwindow.geometry("1080x720")
    menuwindow.title("Monkey: Tears and Blood")
    menuwindow.iconbitmap("Dice-icon.ico")
    menuwindow.resizable(False, False)
    menuwindow.configure(background = "black")

    #Ventana de Juego
    def game():
        gamewindow = tk.Toplevel()
        gamewindow.title("Prepare to Die")
        gamewindow.geometry("1080x720")
        gamewindow.iconbitmap("Dice-icon.ico")
        gamewindow.resizable(False, False)
        gamewindow.configure(background="black")

        #Canvas Principal
        canvasGame = tk.Canvas(gamewindow, width=1080, height=720, borderwidth=0, highlightthickness=0, bg="#072E60")
        canvasGame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #Imagen1/Personaje Principal
        imagePrin = Image.open("toto.png")
        resizedPrin = imagePrin.resize((50, 75), Image.ANTIALIAS)
        nuevoPrin = ImageTk.PhotoImage(resizedPrin, master=canvasGame)
        #principal = canvasGame.create_image(125, 500, image=nuevoPrin, anchor=tk.NW)

        #Platformas
        imagePlat1 = Image.open("platA.png")
        resizedPlat1 = imagePlat1.resize((762,50), Image.ANTIALIAS)
        nuevoPlat1 = ImageTk.PhotoImage(resizedPlat1, master= canvasGame)
        plat1 = canvasGame.create_image(100, 675, image= nuevoPlat1, anchor=tk.NW)

        #Movimiento
        class Totoro:
            def __init__(self, canvas):
                self.canvas = canvas
                self.personaje = canvasGame.create_image(125, 500, image=nuevoPrin, anchor=tk.NW)
                self.x = 0
                self.y = 0
                self.canvas.move(self.personaje, self.x, self.y)
                self.gravity = 0.1
                self.canvasHeight = canvasGame.winfo_height()
                self.canvasWidth = canvasGame.winfo_width()
                self.canvas.bind_all("<Right>", self.right)
                self.canvas.bind_all("<Left>", self.left)
                self.canvas.bind_all("<KeyPress-Up>", self.jump)
                self.canvas.bind_all("<KeyRelease-Up>", self.jump_stop)
                self.jump_counter = 0
                self.move_counter = 0

            def move_player(self):
                pos = self.canvas.coords(self.personaje)
                self.x = 0
                self.y += self.gravity
                self.canvas.move(self.personaje, self.x, self.y)
                if pos[0] <= 0:
                    self.x = 1

                elif pos[2] >= self.canvasWidth:
                    self.x = -1

                elif pos[1] <= 0:
                    self.y = 1

                elif pos[3] >= self.canvasWidth:
                    self.y = 0

            def right(self, evt):
                self.x = 5
                self.y = 0
                self.canvas.move(self.personaje, self.x, self.y)

            def left(self, evt):
                self.x = -5
                self.y = 0
                self.canvas.move(self.personaje, self.x, self.y)

            def jump(self, evt):
                if self.jump_counter < 2:
                    self.y = -6

                    self.jump_counter += 2


            def jump_stop(self, evt):
                self.y = 0

                self.jump_counter = 0
            def gravedad(self):
                self.y += 3.2







        def crear():
            toto = Totoro(canvasGame)
        crear()
        #Puntaucion
        scoreShow = tk.Label(canvasGame, text= "SCORE:"+str(score), bg= "#072E60", fg= "white")
        scoreShow.place(x = 950, y = 25)

        gamewindow.mainloop()

    def leaderboard():
        scorewindow = tk.Toplevel()
        scorewindow.title("Hall of Death")
        scorewindow.geometry("1080x720")
        scorewindow.iconbitmap("Dice-icon.ico")
        scorewindow.resizable(False, False)
        scorewindow.configure(background="black")

        scorewindow.mainloop()

    #Botones
    botonStart=tk.Button(menuwindow, text= "Start the Journey", command=game)
    botonStart.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    botonScore = tk.Button(menuwindow, text="Hall of Death", command=leaderboard)
    botonScore.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    #Titulos


    menuwindow.mainloop()

anim.after(1000, main)  #despues de 5 segundos, llama a main(), que destruye la animacion y arranca el menu
anim.mainloop()
