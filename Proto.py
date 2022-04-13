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
                self.canvas.bind_all("<Up>", self.jump)
                self.jump_counter = 0
                self.move_counter = 0

            def move_player(self):
                pos = self.canvas.coords(self.personaje)
                self.x = 0
                self.y += self.gravity
                self.canvas.move(self.personaje, self.x, self.y)
                if pos[0] <= 0:
                    self.x = 5

                elif pos[2] >= self.canvasWidth:
                    self.x = -5

                elif pos[1] <= 0:
                    self.y = 5

                elif pos[3] >= self.canvasWidth:
                    self.y = -5

            def right(self, evt):
                self.x = 5
                self.y = 0
                self.canvas.move(self.personaje, self.x, self.y)

            def left(self, evt):
                self.x = -5
                self.y = 0
                self.canvas.move(self.personaje, self.x, self.y)

            def jump(self, evt):
                self.x = 0
                diff = 0  ## Difference to initial level
                self.y = -3.7  ## Initial speed in y direction
                grav = .1  ## Gravitation

                while diff >= 0:  ## While it is still jumping (higher than initially)
                    self.canvas.move(self.personaje, self.x, self.y)
                    canvasGame.update()
                    time.sleep(.01)  ## Pause for 1/100 second
                    diff -= self.y  ## Update current jumping height
                    self.y += grav  ## Update the speed in y direction

                y = 5.5  ## Just so it is not moved again, afterwards

                self.canvas.move(self.personaje, self.x, self.y)







        def crear():
            toto = Totoro(canvasGame)
            circle_thread = Thread(target=toto.move_player())
            circle_thread.daemon = True
            circle_thread.start()
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



"""#Movimiento
            def createBarrel():
                barrel = Barrel(canvasGame)
                circle_thread = Thread(target=barrel.movement())
                circle_thread.daemon = True
                circle_thread.start()


            def plzmove():
                moveplz = Thread(target=move())
                moveplz.daemon = True
                moveplz.start()


            def movimiento():
                def left(event):
                    x = -5
                    y = 0
                    canvasGame.update()
                    edgeReached()
                    canvasGame.move(principal,x, y)
                    collision()

                def right(event):
                    x = 5
                    y = 0
                    canvasGame.update()
                    edgeReached()
                    canvasGame.move(principal,x, y)
                    collision()

                def jump(event):
                    x = 0
                    diff = 0  ## Difference to initial level
                    y = -3.7  ## Initial speed in y direction
                    grav = .1  ## Gravitation

                    while diff >= 0:  ## While it is still jumping (higher than initially)
                        canvasGame.move(principal, x, y)
                        canvasGame.update()
                        time.sleep(.01)  ## Pause for 1/100 second
                        diff -= y  ## Update current jumping height
                        y += grav  ## Update the speed in y direction
                        edgeReached()
                        collision()
                    y = 5.5  ## Just so it is not moved again, afterwards
                    edgeReached()
                    canvasGame.move(principal, x, y)
                    collision()

                def score(event):
                    x = 0
                    y = 5
                    edgeReached()
                    canvasGame.move(principal,x, y)
                    collision()

                canvasGame.bind_all("<Left>", left)
                canvasGame.bind_all("<Right>", right)
                canvasGame.bind_all("<Up>", jump)
                canvasGame.bind_all("<Down>", score)

            movimiento()

            def movbarrrel():
                a = 1
                x = 0
                y = 0
                while a == 1:
                    if canvasGame.coords(obs)[0] >= 100:
                        x += 15
                        y = 0
                        movimiento()
                        canvasGame.update()
                        time.sleep(0.05)
                        canvasGame.move(obs, x, y)

                    elif canvasGame.coords(obs)[0] < 0:
                        x -= 15
                        y = 0
                        movimiento()
                        canvasGame.update()
                        time.sleep(0.9)
                        canvasGame.move(obs, x, y)
            movbarrrel() and movimiento() and collision()
            #Generar Barriles
            class Barrel:
                def __init__(self, canvas):
                    self.canvas = canvas
                    self.obstaculo = canvasGame.create_image(125, 500, image=nuevoObs, anchor=tk.NW)
                    self.x = 16
                    self.y = 0

                def movement(self):
                    while True:
                        coords = canvasGame.coords(self.obstaculo)
                        if (coords[0] >= 1000):
                            self.x = -16
                            self.y = 0
                        elif (coords[0] < 0):
                            self.x = 16
                            self.y = 0
                        movimiento()
                        self.canvas.move(self.obstaculo, self.x,self.y)
                        canvasGame.update()
                        time.sleep(0.05)

            def createBarrel():
                barrel = Barrel(canvasGame)
                circle_thread = Thread(target=barrel.movement())
                circle_thread.daemon = True
                circle_thread.start()
                
                #Generar Barriles
            class Barrel:
                def __init__(self, canvas):
                    self.canvas = canvas
                    self.obs = canvasGame.create_image(125, 500, image=nuevoObs, anchor=tk.NW)
                    self.x = 16
                    self.y = 0

                def movement(self):
                    while True:
                        coords = canvasGame.coords(self.obs)
                        if (coords[0] >= 1000):
                            self.x = -10
                            self.y = 0
                        elif (coords[0] < 0):
                            self.x = 10
                            self.y = 0
                        self.canvas.move(self.obs, self.x,self.y)
                        canvasGame.update()
                        time.sleep(0.05)
"""