"""
Proyecto Programado 1 - Esteban Secaida
Monkey: The Last Dream

"""
########################################################################################################################

# Librerias
import tkinter as tk
from PIL import ImageTk, Image
import shelve
import pygame
import random
import time
from threading import Thread
from natsort import natsorted

########################################################################################################################

# Colores
color1 = "blue"
color2 = "green"
color3 = "gray"
color4 = "purple"
color5 = "brown"
colorpool = [color5, color4, color3, color2, color1]

########################################################################################################################

# Variable de Puntuacion
global score
score = 0
# Variable de Vida
global lives
lives = 3
# Variable que impide doble salto
global jumposky
jumposky = 0
# Variables para controlar puntos por plataforma
global udosuno
udosuno = 0
global udosdos
udosdos = 0
global utres
utres = 0
global duno
duno = 0
global ddos
ddos = 0
global dtres
dtres = 0
global dcuatro
dcuatro = 0
global dcinco
dcinco = 0

########################################################################################################################

# Imagen Personaje Principal
imagePrin = Image.open("toto.png")
# Imagen Dama
imageDama = Image.open("chi.png")
# Imagen MonoMalo
imageMonk = Image.open("demonmonkey.png")
# Imagen Obstaculos
imageObs = Image.open("obs1.png")
imageFlame = Image.open("fuego.jpg")
# Imagen Plataforma y Gradas
imagePlat1 = Image.open("platA.png")

########################################################################################################################

# SplashAnimation (Se usaron las ideas presentadas por Codemy.com, de generar el splash por medio de una ventana)
anim = tk.Tk()
anim.geometry("1080x720")
anim.geometry("+250+50")
anim.overrideredirect(True)  # eliminar borde
anim.configure(background="black")
titulo1 = tk.Label(anim, text="The Monkey is the key...but he is also death...a herald of doom...",
                   font="Papyrus", bg="black", fg="white")
titulo1.pack(pady=20)
titulo2 = tk.Label(anim, text="...can you KILL him...he is no longer a monkey, for he is the DEMON MONKEY!",
                   font="Papyrus", bg="black", fg="white")
titulo2.pack(pady=25)
titulo3 = tk.Label(anim, text="Monkey: The Last Dream", font=("Papyrus", 40), bg="black", fg="white")
titulo3.pack(pady=40)
titulo4 = tk.Label(anim, text="Developed by Esteban Secaida", font=("Papyrus", 40), bg="black", fg="white")
titulo4.pack(pady=50)
titulo5 = tk.Label(anim, text="Soundtrack by TWICE and Julieta Venegas",
                   font=("Papyrus", 15), bg="black", fg="white")
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

########################################################################################################################

# Funcion de sonido para la animacion splash"
def playIntro():
    pygame.init()
    pygame.mixer.music.load("introReal.mp3")
    pygame.mixer.music.play(loops=-1)

# Alternativa de sonido para otras pantallas
def playOutro():
    pygame.init()
    pygame.mixer.music.load("bye.mp3")
    pygame.mixer.music.play(loops=0)


########################################################################################################################

# Ventana de Menu
def main():
    # Parametros de Ventana
    anim.destroy()
    playIntro()
    menuwindow = tk.Tk()
    menuwindow.geometry("1080x720")
    menuwindow.geometry("+250+50")
    menuwindow.title("Monkey: The Last Dream")
    menuwindow.iconbitmap("Dice-icon.ico")
    menuwindow.resizable(False, False)
    menuwindow.configure(background="black")

    ####################################################################################################################

    # Función para la musica de mi juego
    def playSound1():
        pygame.init()
        pygame.mixer.music.load("soundtrack.mp3")
        pygame.mixer.music.play(loops=3)
        pygame.mixer.music.play()

    ####################################################################################################################

    # Ventana de Validación antes de entrar al nivel
    def startwindow():
        # Resetear Variables Globales
        global score
        global lives
        global udosuno
        global udosdos
        global utres
        global duno
        global ddos
        global dtres
        global dcuatro
        global dcinco
        score = 0
        lives = 3
        udosuno = 0
        udosdos = 0
        utres = 0
        duno = 0
        ddos = 0
        dtres = 0
        dcuatro = 0
        dcinco = 0

        ################################################################################################################

        # Parametros Ventana
        startWin = tk.Tk()
        startWin.geometry("600x600")
        startWin.geometry("+475+100")
        startWin.title("Prepare to Dream")
        startWin.iconbitmap("Dice-icon.ico")
        startWin.resizable(False, False)
        startWin.configure(background="black")

        ################################################################################################################

        # Canvas
        canvasPepe = tk.Canvas(startWin, width=600, height=600, borderwidth=0, highlightthickness=0, bg="black")
        canvasPepe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ################################################################################################################

        # Funcion efecto mono loco
        def runCreepy():
            image = Image.open("pepemujica.png")
            resized = image.resize((600, 600), Image.ANTIALIAS)
            nuevo = ImageTk.PhotoImage(resized, master=canvasPepe)
            produ = canvasPepe.create_image(0, 0, image=nuevo, anchor=tk.NW)
            startWin.update()
            time.sleep(0.5)
            startWin.after(500, runCreepy)

        runCreepy()

        ################################################################################################################

        # Funcion para entrar al juego
        def nextStep():
            startWin.destroy()
            game1()

        ################################################################################################################

        # Botón
        botonN1 = tk.Button(startWin, text="Enter the Realm of the Monkey!!!!!", command=nextStep)
        botonN1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ################################################################################################################

        startWin.mainloop()

    ####################################################################################################################

    # Ventana para manejar el nivel 1
    def game1():

        ################################################################################################################
        # LLamada a funciones globales
        global score
        global lives

        ################################################################################################################

        # Entrar al nivel 1 si cumple el requisito de vidas
        if lives >= 1:
            playSound1()
            gamewindow = tk.Toplevel()
            gamewindow.title("First Dream")
            gamewindow.geometry("1080x720")
            gamewindow.geometry("+250+50")
            gamewindow.iconbitmap("Dice-icon.ico")
            gamewindow.resizable(False, False)
            gamewindow.configure(background="black")

            ############################################################################################################

            # Canvas Principal
            canvasGame = tk.Canvas(gamewindow, width=1080, height=720, borderwidth=0, highlightthickness=0, bg="black")
            canvasGame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            ############################################################################################################

            # Imagen Personaje Principal
            resizedPrin = imagePrin.resize((50, 75), Image.ANTIALIAS)
            nuevoPrin = ImageTk.PhotoImage(resizedPrin, master=canvasGame)
            principal = canvasGame.create_image(125, 600, image=nuevoPrin, anchor=tk.NW)

            # Imagen Dama
            resizedDama = imageDama.resize((75, 75), Image.ANTIALIAS)
            nuevoDama = ImageTk.PhotoImage(resizedDama, master=canvasGame)
            dama = canvasGame.create_image(225, 163, image=nuevoDama, anchor=tk.NW)

            # Imagen MonoMalo
            resizedMonk = imageMonk.resize((125, 125), Image.ANTIALIAS)
            nuevoMonk = ImageTk.PhotoImage(resizedMonk, master=canvasGame)
            monkeyDemon = canvasGame.create_image(10, 150, image=nuevoMonk, anchor=tk.NW)

            # Imagen Obstaculo
            resizedObs = imageObs.resize((38, 38), Image.ANTIALIAS)
            nuevoObs = ImageTk.PhotoImage(resizedObs, master=canvasGame)
            resizedFlame = imageFlame.resize((38, 38), Image.ANTIALIAS)
            nuevoFlame = ImageTk.PhotoImage(resizedFlame, master=canvasGame)

            # Platformas
            resizedPlat1 = imagePlat1.resize((1080, 50), Image.ANTIALIAS)
            resizedPlat2 = imagePlat1.resize((450, 50), Image.ANTIALIAS)
            nuevoPlat1 = ImageTk.PhotoImage(resizedPlat1, master=canvasGame)
            plat1 = canvasGame.create_image(0, 675, image=nuevoPlat1, anchor=tk.NW)
            nuevoPlat2 = ImageTk.PhotoImage(resizedPlat2, master=canvasGame)
            plat2 = canvasGame.create_image(0, 475, image=nuevoPlat2, anchor=tk.NW)
            plat3 = canvasGame.create_image(545, 475, image=nuevoPlat1, anchor=tk.NW)
            plat4 = canvasGame.create_image(-100, 275, image=nuevoPlat1, anchor=tk.NW)

            # Gradas
            resizedGradA1 = imagePlat1.resize((52, 10), Image.ANTIALIAS)
            resizedGradA2 = imagePlat1.resize((200, 10), Image.ANTIALIAS)
            nuevoGradA1 = ImageTk.PhotoImage(resizedGradA1, master=canvasGame)
            gradaA1 = canvasGame.create_image(475, 485, image=nuevoGradA1, anchor=tk.NW)
            gradaA2 = canvasGame.create_image(475, 545, image=nuevoGradA1, anchor=tk.NW)
            gradaA3 = canvasGame.create_image(475, 608, image=nuevoGradA1, anchor=tk.NW)
            gradaB1 = canvasGame.create_image(1000, 290, image=nuevoGradA1, anchor=tk.NW)
            gradaB2 = canvasGame.create_image(1000, 350, image=nuevoGradA1, anchor=tk.NW)
            gradaB3 = canvasGame.create_image(1000, 410, image=nuevoGradA1, anchor=tk.NW)
            nuevoGradA2 = ImageTk.PhotoImage(resizedGradA2, master=canvasGame)
            gradaC1 = canvasGame.create_image(250, 225, image=nuevoGradA2, anchor=tk.NW)

            ############################################################################################################

            # Comportamiento y parametros de los barriles
            class Barrel:
                def __init__(self, canvas):
                    self.canvas = canvas
                    self.obstaculo = canvasGame.create_image(300, 238, image=nuevoObs, anchor=tk.NW)

                def movement1(self):
                    global score
                    global lives
                    pos = canvasGame.bbox(self.obstaculo)
                    enemy = canvasGame.bbox(principal)
                    if (2 < (pos[1] - enemy[3]) < 35) and \
                            ((1 < abs(pos[0] - enemy[0]) < 10) or
                             (1 < abs(pos[2] - enemy[2]) < 10)):
                        score += 100
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +100 enemy points!",
                                            bg=random.choice(colorpool))
                        gamewindow.after(100, self.movement1)

                        if enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[2] < enemy[2]:
                            score -= 10
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow.destroy()
                            game1()
                        elif enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[0] < enemy[2]:
                            score -= 10
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow.destroy()
                            game1()
                            canvasGame.move(principal, 0, -5)  # ojo esto
                        elif pos[0] <= 980 and pos[1] == 238:
                            # print("P"+str(pos))
                            # print("T"+str(enemy))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= 980 and pos[1] <= 420:
                            # print("2" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= 480 and pos[1] >= 420:
                            # print("3" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] <= 480 and pos[1] <= 620:
                            # print("4" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= -50 and pos[1] >= 620:
                            # print("5" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                    else:
                        if enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[2] < enemy[2]:
                            score -= 10
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow.destroy()
                            game1()
                        elif enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[0] < enemy[2]:
                            score -= 10
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow.destroy()
                            game1()
                            canvasGame.move(principal, 0, -5)  # ojo esto
                        elif pos[0] <= 980 and pos[1] == 238:
                            # print("P"+str(pos))
                            # print("T"+str(enemy))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= 980 and pos[1] <= 420:
                            # print("2" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= 480 and pos[1] >= 420:
                            # print("3" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] <= 480 and pos[1] <= 620:
                            # print("4" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= -50 and pos[1] >= 620:
                            # print("5" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)

            # Comportamiento y parametros de las llamas
            class Flame:
                def __init__(self, canvas):
                    self.canvas = canvas
                    self.flame = canvasGame.create_image(300, 238, image=nuevoFlame, anchor=tk.NW)

                def movement1(self):
                    global score
                    global lives
                    pos = canvasGame.bbox(self.flame)
                    enemy = canvasGame.bbox(principal)
                    if ((pos[1] - enemy[3]) > 2 and (pos[1] - enemy[3]) < 35) and \
                            ((abs(pos[0] - enemy[0]) > 1 and abs(pos[0] - enemy[0]) < 10) or
                             (abs(pos[2] - enemy[2]) > 1 and abs(pos[2] - enemy[2]) < 10)):
                        score += 100
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +100 enemy points!",
                                            bg=random.choice(colorpool))
                        gamewindow.after(100, self.movement1)

                        if enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[2] < enemy[2]:
                            score -= 10
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow.destroy()
                            game1()
                        elif enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[0] < enemy[2]:
                            score -= 10
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow.destroy()
                            game1()
                            canvasGame.move(principal, 0, -5)  # ojo esto
                        elif pos[0] <= 980 and pos[1] == 238:
                            # print("P"+str(pos))
                            # print("T"+str(enemy))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= 980 and pos[1] <= 420:
                            # print("2" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= 480 and pos[1] >= 420:
                            # print("3" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] <= 480 and pos[1] <= 620:
                            # print("4" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= -50 and pos[1] >= 620:
                            # print("5" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                    else:
                        if enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[2] < enemy[2]:
                            score -= 10
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow.destroy()
                            game1()
                        elif enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[0] < enemy[2]:
                            score -= 10
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow.destroy()
                            game1()
                            canvasGame.move(principal, 0, -5)  # ojo esto
                        elif pos[0] <= 980 and pos[1] == 238:
                            # print("P"+str(pos))
                            # print("T"+str(enemy))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= 980 and pos[1] <= 420:
                            # print("2" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= 480 and pos[1] >= 420:
                            # print("3" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] <= 480 and pos[1] <= 620:
                            # print("4" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)
                        elif pos[0] >= -50 and pos[1] >= 620:
                            # print("5" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow.update()
                            gamewindow.after(100, self.movement1)

            def createBarrel():
                barrel = Barrel(canvasGame)
                barrel_thread = Thread(target=barrel.movement1())
                barrel_thread.daemon = True
                barrel_thread.start()
                gamewindow.after(random.randint(11000, 19000), createBarrel)

            def createFlame():
                flame = Flame(canvasGame)
                flame_thread = Thread(target=flame.movement1())
                flame_thread.daemon = True
                flame_thread.start()
                gamewindow.after(random.randint(8000, 15000), createFlame)

            ############################################################################################################

            # Funcion que le da gravedad al personaje principal en el nivel 1
            def gravity():
                x = 0
                y = 2
                canvasGame.update()
                edgeReached()
                canvasGame.move(principal, x, y)
                collision()
                gamewindow.after(100, gravity)

            # Funcion que permite el movimiento del jugador en el nivel 1
            def move():
                def left(event):
                    x = -10
                    y = 0
                    canvasGame.update()
                    edgeReached()
                    canvasGame.move(principal, x, y)
                    collision()

                def right(event):
                    x = 10
                    y = 0
                    canvasGame.update()
                    edgeReached()
                    canvasGame.move(principal, x, y)
                    collision()

                def jump(event):
                    global jumposky
                    if jumposky != 0:
                        jumposky = 0
                        x = 0
                        y = -65
                        edgeReached()
                        canvasGame.update()
                        canvasGame.move(principal, x, y)
                        collision()

                def down(event):
                    x = 0
                    y = 2
                    edgeReached()
                    canvasGame.move(principal, x, y)
                    collision()

                canvasGame.bind_all("<Left>", left)
                canvasGame.bind_all("<Right>", right)
                canvasGame.bind_all("<Up>", jump)
                canvasGame.bind_all("<Down>", down)

            ############################################################################################################

            # Colisiones
            def collision():
                princol = canvasGame.bbox(principal)
                damacol = canvasGame.bbox(dama)
                moncol = canvasGame.bbox(monkeyDemon)
                plat1col = canvasGame.bbox(plat1)
                plat2col = canvasGame.bbox(plat2)
                plat3col = canvasGame.bbox(plat3)
                plat4col = canvasGame.bbox(plat4)
                gradaA1col = canvasGame.bbox(gradaA1)
                gradaA2col = canvasGame.bbox(gradaA2)
                gradaA3col = canvasGame.bbox(gradaA3)
                gradaB1col = canvasGame.bbox(gradaB1)
                gradaB2col = canvasGame.bbox(gradaB2)
                gradaB3col = canvasGame.bbox(gradaB3)
                gradaC1col = canvasGame.bbox(gradaC1)

                ########################################################################################################

                global score
                global lives
                global jumposky
                global udosuno
                global udosdos
                global utres

                ########################################################################################################

                # Dama
                if damacol[0] < princol[0] < damacol[2] and damacol[1] < princol[3] < damacol[3]:
                    score += 900
                    scoreShow.configure(text="SCORE: " + str(score))
                    time.sleep(1.0)
                    gamewindow.destroy()
                    game2()

                # Mono
                elif moncol[0] < princol[0] < moncol[2] and moncol[1] < princol[3] < moncol[3]:
                    score -= 250
                    lives -= 1
                    scoreShow.configure(text="SCORE: " + str(score))
                    livesShow.configure(text="LIVES: " + str(lives))
                    time.sleep(1.0)
                    gamewindow.destroy()
                    game1()

                # Primera Plataforma
                elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[0] < plat1col[2] \
                        and plat1col[0] < princol[2] < plat1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[0] < plat1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[2] < plat1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # Segunda Plataforma
                elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2] \
                        and plat2col[0] < princol[2] < plat2col[2]:
                    jumposky += 1
                    if udosuno == 0:
                        score += 500
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +500 platform points!",
                                            bg=random.choice(colorpool))
                        udosuno += 1
                    canvasGame.move(principal, 0, -2)
                elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[2] < plat2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2] \
                        and plat2col[0] < princol[2] < plat2col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[2] < plat2col[2]:
                    canvasGame.move(principal, 0, 20)
                elif princol[1] < plat2col[1] < princol[3] and princol[0] < plat2col[2] < princol[2] and \
                        princol[1] < plat2col[3] < princol[3]:  # Colicion con la parte derecha
                    canvasGame.move(principal, 10, 0)

                # Tercera Plataforma
                elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2] \
                        and plat3col[0] < princol[2] < plat3col[2]:
                    jumposky += 1
                    if udosdos == 0:
                        score += 500
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +500 platform points!",
                                            bg=random.choice(colorpool))
                        udosdos += 1
                    canvasGame.move(principal, 0, -2)
                elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[2] < plat3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2] \
                        and plat3col[0] < princol[2] < plat3col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[2] < plat3col[2]:
                    canvasGame.move(principal, 0, 20)
                elif princol[1] < plat3col[1] < princol[3] and princol[0] < plat3col[0] < princol[2] and \
                        princol[1] < plat3col[3] < princol[3]:  # Colicion con la parte izquierda
                    canvasGame.move(principal, -10, 0)

                # Cuarta Plataforma
                elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2] \
                        and plat4col[0] < princol[2] < plat4col[2]:
                    jumposky += 1
                    if utres == 0:
                        score += 1000
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +1000 platform points!",
                                            bg=random.choice(colorpool))
                        utres += 1
                    canvasGame.move(principal, 0, -2)
                elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[2] < plat4col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2] \
                        and plat4col[0] < princol[2] < plat4col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[2] < plat4col[2]:
                    canvasGame.move(principal, 0, 20)
                elif princol[1] < plat4col[1] < princol[3] and princol[0] < plat4col[2] < princol[2] and \
                        princol[1] < plat4col[3] < princol[3]:
                    canvasGame.move(principal, 10, 0)

                # GradaA1
                elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[0] < gradaA1col[2] \
                        and gradaA1col[0] < princol[2] < gradaA1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[0] < gradaA1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[2] < gradaA1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaA2
                elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[0] < gradaA2col[2] \
                        and gradaA2col[0] < princol[2] < gradaA2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[0] < gradaA2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[2] < gradaA2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaA3
                elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[0] < gradaA3col[2] \
                        and gradaA3col[0] < princol[2] < gradaA3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[0] < gradaA3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[2] < gradaA3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaB1
                elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[0] < gradaB1col[2] \
                        and gradaB1col[0] < princol[2] < gradaB1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[0] < gradaB1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[2] < gradaB1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaB2
                elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[0] < gradaB2col[2] \
                        and gradaB2col[0] < princol[2] < gradaB2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[0] < gradaB2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[2] < gradaB2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaB3
                elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[0] < gradaB3col[2] \
                        and gradaB3col[0] < princol[2] < gradaB3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[0] < gradaB3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[2] < gradaB3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaC1
                elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[0] < gradaC1col[2] \
                        and gradaB3col[0] < princol[2] < gradaB3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[0] < gradaC1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[2] < gradaC1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

            ############################################################################################################

            # Personaje no se salga de la ventana
            def edgeReached():
                boundary = canvasGame.bbox(principal)
                prinleft = boundary[0]
                prinright = boundary[2]
                printop = boundary[1]
                prinbottom = boundary[3]
                if prinleft < 0:
                    canvasGame.move(principal, 10, 0)
                elif prinright > 1080:
                    canvasGame.move(principal, -10, 0)
                elif printop < 0:
                    canvasGame.move(principal, 0, 20)
                elif prinbottom > 720:
                    canvasGame.move(principal, 0, -20)

            ############################################################################################################

            # Puntuación
            scoreShow = tk.Label(canvasGame, text="SCORE: " + str(score), bg="#072E60", fg="white")
            scoreShow.place(x=950, y=25)

            ############################################################################################################

            # Vidas
            livesShow = tk.Label(canvasGame, text="LIVES: " + str(lives), bg="black", fg="white")
            livesShow.place(x=100, y=25)

            ############################################################################################################

            # Puntos que gano
            scorePlus = tk.Label(canvasGame, text="POINTS GAINED THIS LEVEL!: 0", bg="black", fg="white")
            scorePlus.place(x=650, y=25)

            ############################################################################################################

            # Nivel
            showLevel = tk.Label(canvasGame, text="LEVEL 1", bg="black", fg="white")
            showLevel.place(x=400, y=25)

            ############################################################################################################

            move()
            createBarrel()
            createFlame()
            gravity()
            gamewindow.mainloop()

            ############################################################################################################

        # Ventana cuando se pierde en el nivel 1
        else:
            playOutro()
            lives = 3  # esto nos permite volver a tener 3 vidas
            endwindow1 = tk.Toplevel()
            endwindow1.title("You Lost!")
            endwindow1.geometry("1080x720")
            endwindow1.iconbitmap("Dice-icon.ico")
            endwindow1.resizable(False, False)
            endwindow1.configure(background="black")

            ############################################################################################################

            # Canvas
            canvasL1 = tk.Canvas(endwindow1, width=1080, height=720, borderwidth=0, highlightthickness=0, bg="black")
            canvasL1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            ############################################################################################################

            # Imagen
            jordan = Image.open("jordan.jpg")
            jordanres = jordan.resize((1080, 720), Image.ANTIALIAS)
            jordanw = ImageTk.PhotoImage(jordanres, master=canvasMenu)
            jordanlisto = canvasL1.create_image(0, 0, image=jordanw, anchor=tk.NW)

            ############################################################################################################

            # Entry de Jugador
            entryName = tk.Entry(canvasL1)
            entryName.place(x=475, y=305)

            ############################################################################################################

            # Funcion para guardar puntuación

            def savedata():
                global score
                scores = open("scores.txt", "a")
                scores.write(str(score) + " - " + str(entryName.get()) + ",")
                scores.close()
                endwindow1.destroy()
                score = 0

            ############################################################################################################

            # Puntuacion Final
            scoreShow = tk.Label(canvasL1, text="Final Score: " + str(score), font=("Arial", "30"), bg="black",
                                 fg="white")
            scoreShow.place(x=350, y=150)

            ############################################################################################################

            # Titulo
            label1 = tk.Label(canvasL1, text="Enter Your Name: ", font=("Arial", 15), bg="black", fg="white")
            label1.place(x=300, y=300)

            ############################################################################################################

            # Botón
            botonSave = tk.Button(canvasL1, text="Save Your Stats!", command=savedata)
            botonSave.place(x=675, y=315, anchor=tk.CENTER)

            ############################################################################################################

            endwindow1.mainloop()

    ####################################################################################################################

    "Ventana para manejar el nivel 2"

    def game2():
        global score
        global lives
        # Entrar al nivel 2 si cumple el requisito de vidas
        if lives >= 1:
            playSound1()
            gamewindow2 = tk.Tk()
            gamewindow2.title("Second Dream")
            gamewindow2.geometry("1080x720")
            gamewindow2.geometry("+250+50")
            gamewindow2.iconbitmap("Dice-icon.ico")
            gamewindow2.resizable(False, False)
            gamewindow2.configure(background="black")

            # Canvas Principal
            canvasGame = tk.Canvas(gamewindow2, width=1080, height=720, borderwidth=0, highlightthickness=0,
                                   bg="black")
            canvasGame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            # Imagen1/Personaje Principal
            resizedPrin = imagePrin.resize((40, 65), Image.ANTIALIAS)
            nuevoPrin = ImageTk.PhotoImage(resizedPrin, master=canvasGame)
            principal = canvasGame.create_image(125, 600, image=nuevoPrin, anchor=tk.NW)

            # Imagen Dama
            resizedDama = imageDama.resize((50, 50), Image.ANTIALIAS)
            nuevoDama = ImageTk.PhotoImage(resizedDama, master=canvasGame)
            dama = canvasGame.create_image(225, 63, image=nuevoDama, anchor=tk.NW)

            # Imagen MonoMalo
            resizedMonk = imageMonk.resize((100, 100), Image.ANTIALIAS)
            nuevoMonk = ImageTk.PhotoImage(resizedMonk, master=canvasGame)
            monkeyDemon = canvasGame.create_image(10, 75, image=nuevoMonk, anchor=tk.NW)

            # Imagen Obstáculo
            resizedObs = imageObs.resize((40, 40), Image.ANTIALIAS)
            nuevoObs = ImageTk.PhotoImage(resizedObs, master=canvasGame)
            # obs = canvasGame.create_image(500, 220, image=nuevoObs, anchor=tk.NW)
            resizedFlame = imageFlame.resize((40, 40), Image.ANTIALIAS)
            nuevoFlame = ImageTk.PhotoImage(resizedFlame, master=canvasGame)

            # Plataformas
            resizedPlat1 = imagePlat1.resize((1080, 50), Image.ANTIALIAS)
            nuevoPlat1 = ImageTk.PhotoImage(resizedPlat1, master=canvasGame)
            plat1 = canvasGame.create_image(0, 675, image=nuevoPlat1, anchor=tk.NW)  # nivel1
            resizedPlat2 = imagePlat1.resize((1080, 25), Image.ANTIALIAS)
            nuevoPlat2 = ImageTk.PhotoImage(resizedPlat2, master=canvasGame)
            resizedPlat3 = imagePlat1.resize((400, 25), Image.ANTIALIAS)
            nuevoPlat3 = ImageTk.PhotoImage(resizedPlat3, master=canvasGame)
            plat2 = canvasGame.create_image(-100, 525, image=nuevoPlat2, anchor=tk.NW)  # nivel2
            plat3 = canvasGame.create_image(200, 375, image=nuevoPlat2, anchor=tk.NW)  # nivel3
            plat4 = canvasGame.create_image(0, 225, image=nuevoPlat3, anchor=tk.NW)  # nivel4
            plat5 = canvasGame.create_image(-1000, 375, image=nuevoPlat2, anchor=tk.NW)  # nivel3
            plat6 = canvasGame.create_image(575, 225, image=nuevoPlat3, anchor=tk.NW)  # nivel4

            # Gradas
            resizedGradA1 = imagePlat1.resize((52, 10), Image.ANTIALIAS)
            nuevoGradA1 = ImageTk.PhotoImage(resizedGradA1, master=canvasGame)
            gradaA1 = canvasGame.create_image(115, 475, image=nuevoGradA1, anchor=tk.NW)
            gradaA2 = canvasGame.create_image(1000, 575, image=nuevoGradA1, anchor=tk.NW)
            gradaA3 = canvasGame.create_image(1000, 615, image=nuevoGradA1, anchor=tk.NW)
            gradaB1 = canvasGame.create_image(1000, 285, image=nuevoGradA1, anchor=tk.NW)
            gradaB2 = canvasGame.create_image(1000, 325, image=nuevoGradA1, anchor=tk.NW)
            gradaB3 = canvasGame.create_image(115, 440, image=nuevoGradA1, anchor=tk.NW)
            resizedGradA2 = imagePlat1.resize((200, 10), Image.ANTIALIAS)
            nuevoGradA2 = ImageTk.PhotoImage(resizedGradA2, master=canvasGame)
            gradaC1 = canvasGame.create_image(250, 125, image=nuevoGradA2, anchor=tk.NW)
            resizedGradA3 = imagePlat1.resize((100, 10), Image.ANTIALIAS)
            nuevoGradA3 = ImageTk.PhotoImage(resizedGradA3, master=canvasGame)
            gradaD1 = canvasGame.create_image(440, 240, image=nuevoGradA3, anchor=tk.NW)
            gradaD2 = canvasGame.create_image(515, 185, image=nuevoGradA1, anchor=tk.NW)
            gradaD3 = canvasGame.create_image(515, 140, image=nuevoGradA1, anchor=tk.NW)

            # Movimiento Jugador y Barriles
            class Barrel:
                def __init__(self, canvas):
                    self.canvas = canvas
                    self.obstaculo = canvasGame.create_image(300, 185, image=nuevoObs, anchor=tk.NW)

                def movement1(self):
                    global score
                    global lives
                    pos = canvasGame.bbox(self.obstaculo)
                    enemy = canvasGame.bbox(principal)
                    if (2 < (pos[1] - enemy[3]) < 35) and \
                            ((1 < abs(pos[0] - enemy[0]) < 10) or
                             (1 < abs(pos[2] - enemy[2]) < 10)):
                        score += 200
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +200 enemy points!",
                                            bg=random.choice(colorpool))
                        if enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[2] < enemy[2]:
                            score -= 15
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow2.destroy()
                            game2()
                        elif enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[0] < enemy[2]:
                            score -= 15
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow2.destroy()
                            game2()
                            canvasGame.move(principal, 0, -5)
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] <= 980 and pos[1] == 185:
                            # print("P"+str(pos))
                            # print("T"+str(enemy))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 980 and pos[1] <= 325:
                            # print("2" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 480 and pos[1] >= 325 and pos[1] < 480:
                            # print("3" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] <= 480 and pos[1] <= 480:
                            # print("4" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] <= 1000 and pos[1] >= 480 and pos[1] < 615:
                            # print("5" + str(pos))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 1000 and pos[1] <= 625:
                            # print("6" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= -50 and pos[1] >= 625:
                            # print("7" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                    else:
                        if enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[2] < enemy[2]:
                            score -= 15
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow2.destroy()
                            game2()
                        elif enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[0] < enemy[2]:
                            score -= 15
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow2.destroy()
                            game2()
                            canvasGame.move(principal, 0, -5)
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] <= 980 and pos[1] == 185:
                            # print("P"+str(pos))
                            # print("T"+str(enemy))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 980 and pos[1] <= 325:
                            # print("2" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 480 and pos[1] >= 325 and pos[1] < 480:
                            # print("3" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] <= 480 and pos[1] <= 480:
                            # print("4" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] <= 1000 and pos[1] >= 480 and pos[1] < 615:
                            # print("5" + str(pos))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 1000 and pos[1] <= 625:
                            # print("6" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= -50 and pos[1] >= 625:
                            # print("7" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.obstaculo, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)

            class Flame:
                def __init__(self, canvas):
                    self.canvas = canvas
                    self.flame = canvasGame.create_image(300, 185, image=nuevoFlame, anchor=tk.NW)

                def movement1(self):
                    global score
                    global lives
                    pos = canvasGame.bbox(self.flame)
                    enemy = canvasGame.bbox(principal)
                    if (2 < (pos[1] - enemy[3]) < 35) and \
                            ((1 < abs(pos[0] - enemy[0]) < 10) or
                             (1 < abs(pos[2] - enemy[2]) < 10)):
                        score += 250
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +250 enemy points!",
                                            bg=random.choice(colorpool))
                        gamewindow2.after(100, self.movement1)
                        if enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[2] < enemy[2]:
                            score -= 20
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow2.destroy()
                            game2()
                        elif enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[0] < enemy[2]:
                            score -= 20
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow2.destroy()
                            game2()
                            canvasGame.move(principal, 0, -5)
                        elif pos[0] <= 470 and pos[1] == 185:
                            # print("P"+str(pos))
                            # print("T"+str(enemy))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 470 and pos[1] <= 325:
                            # print("2" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 175 and pos[1] >= 325:
                            # print("3" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] <= 175 and pos[1] <= 480:
                            # print("4" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= -50 and pos[1] >= 480:
                            # print("5" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                    else:
                        if enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[2] < enemy[2]:
                            score -= 20
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow2.destroy()
                            game2()
                        elif enemy[1] < pos[1] < enemy[3] and enemy[0] < pos[0] < enemy[2]:
                            score -= 20
                            lives -= 1
                            scoreShow.configure(text="SCORE: " + str(score))
                            livesShow.configure(text="LIVES: " + str(lives))
                            time.sleep(1.0)
                            gamewindow2.destroy()
                            game2()
                            canvasGame.move(principal, 0, -5)
                        elif pos[0] <= 470 and pos[1] == 185:
                            # print("P"+str(pos))
                            # print("T"+str(enemy))
                            barrelx = 20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 470 and pos[1] <= 325:
                            # print("2" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= 175 and pos[1] >= 325:
                            # print("3" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] <= 175 and pos[1] <= 480:
                            # print("4" + str(pos))
                            barrelx = 0
                            barrely = 20
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)
                        elif pos[0] >= -50 and pos[1] >= 480:
                            # print("5" + str(pos))
                            barrelx = -20
                            barrely = 0
                            canvasGame.move(self.flame, barrelx, barrely)
                            gamewindow2.update()
                            gamewindow2.after(100, self.movement1)

            def createBarrel():
                barrel = Barrel(canvasGame)
                barrel_thread = Thread(target=barrel.movement1())
                barrel_thread.daemon = True
                barrel_thread.start()
                gamewindow2.after(random.randint(9000, 11000), createBarrel)

            def createFlame():
                flame = Flame(canvasGame)
                flame_thread = Thread(target=flame.movement1())
                flame_thread.daemon = True
                flame_thread.start()
                gamewindow2.after(random.randint(5000, 9000), createFlame)

            def gravity():
                x = 0
                y = 2
                canvasGame.update()
                edgeReached()
                canvasGame.move(principal, x, y)
                collision()
                gamewindow2.after(100, gravity)

            def move():
                def left(event):
                    x = -10
                    y = 0
                    canvasGame.update()
                    edgeReached()
                    canvasGame.move(principal, x, y)
                    collision()

                def right(event):
                    x = 10
                    y = 0
                    canvasGame.update()
                    edgeReached()
                    canvasGame.move(principal, x, y)
                    collision()

                def jump(event):
                    global jumposky
                    if jumposky != 0:
                        jumposky = 0
                        x = 0
                        y = -55
                        edgeReached()
                        canvasGame.update()
                        canvasGame.move(principal, x, y)
                        collision()

                def score(event):
                    x = 0
                    y = 2
                    edgeReached()
                    canvasGame.move(principal, x, y)
                    collision()

                canvasGame.bind_all("<Left>", left)
                canvasGame.bind_all("<Right>", right)
                canvasGame.bind_all("<Up>", jump)
                canvasGame.bind_all("<Down>", score)

            # Colisiones
            def collision():
                princol = canvasGame.bbox(principal)
                damacol = canvasGame.bbox(dama)
                moncol = canvasGame.bbox(monkeyDemon)
                plat1col = canvasGame.bbox(plat1)
                plat2col = canvasGame.bbox(plat2)
                plat3col = canvasGame.bbox(plat3)
                plat4col = canvasGame.bbox(plat4)
                plat5col = canvasGame.bbox(plat5)
                plat6col = canvasGame.bbox(plat6)
                gradaA1col = canvasGame.bbox(gradaA1)
                gradaA2col = canvasGame.bbox(gradaA2)
                gradaA3col = canvasGame.bbox(gradaA3)
                gradaB1col = canvasGame.bbox(gradaB1)
                gradaB2col = canvasGame.bbox(gradaB2)
                gradaB3col = canvasGame.bbox(gradaB3)
                gradaC1col = canvasGame.bbox(gradaC1)
                gradaD1col = canvasGame.bbox(gradaD1)
                gradaD2col = canvasGame.bbox(gradaD2)
                gradaD3col = canvasGame.bbox(gradaD3)

                global score
                global lives
                global jumposky
                global duno
                global ddos
                global dtres
                global dcuatro
                global dcinco

                # Dama
                if damacol[0] < princol[0] < damacol[2] and damacol[1] < princol[3] < damacol[3]:
                    score += 900
                    scoreShow.configure(text="SCORE: " + str(score))
                    time.sleep(1.0)
                    gamewindow2.destroy()
                    congrats()

                # Mono
                elif moncol[0] < princol[0] < moncol[2] and moncol[1] < princol[3] < moncol[3]:
                    score -= 250
                    lives -= 1
                    scoreShow.configure(text="SCORE: " + str(score))
                    livesShow.configure(text="LIVES: " + str(lives))
                    time.sleep(1.0)
                    gamewindow2.destroy()
                    game2()

                # Primera Plataforma
                elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[0] < plat1col[2] \
                        and plat1col[0] < princol[2] < plat1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[0] < plat1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[2] < plat1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # Segunda Plataforma
                elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2] \
                        and plat2col[0] < princol[2] < plat2col[2]:
                    jumposky += 1
                    if duno == 0:
                        score += 1000
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +1000 platform points!",
                                            bg=random.choice(colorpool))
                        duno += 1
                    canvasGame.move(principal, 0, -2)
                elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[2] < plat2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2] \
                        and plat2col[0] < princol[2] < plat2col[2]:
                    canvasGame.move(principal, 0, 50)
                elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2]:
                    canvasGame.move(principal, 0, 50)
                elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[2] < plat2col[2]:
                    canvasGame.move(principal, 0, 50)
                elif princol[1] < plat2col[1] < princol[3] and princol[0] < plat2col[2] < princol[2] and \
                        princol[1] < plat2col[3] < princol[3]:  # Colicion con la parte derecha
                    canvasGame.move(principal, 10, 0)

                # Tercera Plataforma
                elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2] \
                        and plat3col[0] < princol[2] < plat3col[2]:
                    jumposky += 1
                    if ddos == 0:
                        score += 1100
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +1100 platform points!",
                                            bg=random.choice(colorpool))
                        ddos += 1
                    canvasGame.move(principal, 0, -2)
                elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[2] < plat3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2] \
                        and plat3col[0] < princol[2] < plat3col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[2] < plat3col[2]:
                    canvasGame.move(principal, 0, 20)
                elif princol[1] < plat3col[1] < princol[3] and princol[0] < plat3col[0] < princol[2] and \
                        princol[1] < plat3col[3] < princol[3]:  # Colicion con la parte izquierda
                    canvasGame.move(principal, -10, 0)

                # Cuarta Plataforma
                elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2] \
                        and plat4col[0] < princol[2] < plat4col[2]:
                    jumposky += 1
                    if dtres == 0:
                        score += 1200
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +1200 platform points!",
                                            bg=random.choice(colorpool))
                        dtres += 1
                    canvasGame.move(principal, 0, -2)
                elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[2] < plat4col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2] \
                        and plat4col[0] < princol[2] < plat4col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[2] < plat4col[2]:
                    canvasGame.move(principal, 0, 20)
                elif princol[1] < plat4col[1] < princol[3] and princol[0] < plat4col[2] < princol[2] and \
                        princol[1] < plat4col[3] < princol[3]:
                    canvasGame.move(principal, 10, 0)

                # Quinta Plataforma
                elif plat5col[1] < princol[3] < plat5col[3] and plat5col[0] < princol[0] < plat5col[2] \
                        and plat5col[0] < princol[2] < plat5col[2]:
                    jumposky += 1
                    if dcuatro == 0:
                        score += 1300
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +1300 platform points!",
                                            bg=random.choice(colorpool))
                        dcuatro += 1
                    canvasGame.move(principal, 0, -2)
                elif plat5col[1] < princol[3] < plat5col[3] and plat5col[0] < princol[0] < plat5col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat5col[1] < princol[3] < plat5col[3] and plat5col[0] < princol[2] < plat5col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat5col[1] < princol[1] < plat5col[3] and plat5col[0] < princol[0] < plat5col[2] \
                        and plat5col[0] < princol[2] < plat5col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat5col[1] < princol[1] < plat5col[3] and plat5col[0] < princol[0] < plat5col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat5col[1] < princol[1] < plat5col[3] and plat5col[0] < princol[2] < plat5col[2]:
                    canvasGame.move(principal, 0, 20)
                elif princol[1] < plat5col[1] < princol[3] and princol[0] < plat5col[2] < princol[2] and \
                        princol[1] < plat5col[3] < princol[3]:
                    canvasGame.move(principal, 10, 0)

                # Sexta Plataforma
                elif plat6col[1] < princol[3] < plat6col[3] and plat6col[0] < princol[0] < plat6col[2] \
                        and plat6col[0] < princol[2] < plat6col[2]:
                    jumposky += 1
                    if dcinco == 0:
                        score += 2000
                        scoreShow.configure(text="SCORE: " + str(score))
                        scorePlus.configure(text="Last Score Points Gained: +2000 platform points!",
                                            bg=random.choice(colorpool))
                        dcinco += 1
                    canvasGame.move(principal, 0, -2)
                elif plat6col[1] < princol[3] < plat6col[3] and plat6col[0] < princol[0] < plat6col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat6col[1] < princol[3] < plat6col[3] and plat6col[0] < princol[2] < plat6col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif plat6col[1] < princol[1] < plat6col[3] and plat6col[0] < princol[0] < plat6col[2] \
                        and plat6col[0] < princol[2] < plat6col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat6col[1] < princol[1] < plat6col[3] and plat6col[0] < princol[0] < plat6col[2]:
                    canvasGame.move(principal, 0, 20)
                elif plat6col[1] < princol[1] < plat6col[3] and plat6col[0] < princol[2] < plat6col[2]:
                    canvasGame.move(principal, 0, 20)
                elif princol[1] < plat6col[1] < princol[3] and princol[0] < plat6col[2] < princol[2] and \
                        princol[1] < plat6col[3] < princol[3]:
                    canvasGame.move(principal, 10, 0)

                # GradaA1
                elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[0] < gradaA1col[2] \
                        and gradaA1col[0] < princol[2] < gradaA1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[0] < gradaA1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[2] < gradaA1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaA2
                elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[0] < gradaA2col[2] \
                        and gradaA2col[0] < princol[2] < gradaA2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[0] < gradaA2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[2] < gradaA2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaA3
                elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[0] < gradaA3col[2] \
                        and gradaA3col[0] < princol[2] < gradaA3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[0] < gradaA3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[2] < gradaA3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaB1
                elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[0] < gradaB1col[2] \
                        and gradaB1col[0] < princol[2] < gradaB1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[0] < gradaB1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[2] < gradaB1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaB2
                elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[0] < gradaB2col[2] \
                        and gradaB2col[0] < princol[2] < gradaB2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[0] < gradaB2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[2] < gradaB2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaB3
                elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[0] < gradaB3col[2] \
                        and gradaB3col[0] < princol[2] < gradaB3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[0] < gradaB3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[2] < gradaB3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaC1
                elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[0] < gradaC1col[2] \
                        and gradaB3col[0] < princol[2] < gradaB3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[0] < gradaC1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[2] < gradaC1col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaD1
                elif gradaD1col[1] < princol[1] < gradaD1col[3] and gradaD1col[0] < princol[0] < gradaD1col[2] \
                        and gradaB3col[0] < princol[2] < gradaB3col[2]:
                    canvasGame.move(principal, 0, 20)
                elif gradaD1col[1] < princol[1] < gradaD1col[3] and gradaD1col[0] < princol[0] < gradaD1col[2]:
                    canvasGame.move(principal, 0, 20)
                elif gradaD1col[1] < princol[1] < gradaD1col[3] and gradaD1col[0] < princol[2] < gradaD1col[2]:
                    canvasGame.move(principal, 0, 20)

                # GradaD2
                elif gradaD2col[1] < princol[3] < gradaD2col[3] and gradaD2col[0] < princol[0] < gradaD2col[2] \
                        and gradaD2col[0] < princol[2] < gradaD2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaD2col[1] < princol[3] < gradaD2col[3] and gradaD2col[0] < princol[0] < gradaD2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaD2col[1] < princol[3] < gradaD2col[3] and gradaD2col[0] < princol[2] < gradaD2col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

                # GradaD3
                elif gradaD3col[1] < princol[3] < gradaD3col[3] and gradaD3col[0] < princol[0] < gradaD3col[2] \
                        and gradaD3col[0] < princol[2] < gradaD3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaD3col[1] < princol[3] < gradaD3col[3] and gradaD3col[0] < princol[0] < gradaD3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)
                elif gradaD3col[1] < princol[3] < gradaD3col[3] and gradaD3col[0] < princol[2] < gradaD3col[2]:
                    jumposky += 1
                    canvasGame.move(principal, 0, -2)

            # Personaje no se salga de la ventana
            def edgeReached():
                boundary = canvasGame.bbox(principal)
                prinleft = boundary[0]
                prinright = boundary[2]
                printop = boundary[1]
                prinbottom = boundary[3]
                if prinleft < 0:
                    canvasGame.move(principal, 10, 0)
                elif prinright > 1080:
                    canvasGame.move(principal, -10, 0)
                elif printop < 0:
                    canvasGame.move(principal, 0, 20)
                elif prinbottom > 720:
                    canvasGame.move(principal, 0, -20)

            # Puntaucion

            scoreShow = tk.Label(canvasGame, text="SCORE: " + str(score), bg="#072E60", fg="white")
            scoreShow.place(x=950, y=25)

            # Vidas

            livesShow = tk.Label(canvasGame, text="LIVES: " + str(lives), bg="black", fg="white")
            livesShow.place(x=100, y=25)

            # Puntos que gano
            scorePlus = tk.Label(canvasGame, text="POINTS GAINED THIS LEVEL!: 0", bg="black", fg="white")
            scorePlus.place(x=650, y=25)

            # Nivel
            showLevel = tk.Label(canvasGame, text="LEVEL 2", bg="black", fg="white")
            showLevel.place(x=400, y=25)

            move()
            createBarrel()
            createFlame()
            gravity()
            gamewindow2.mainloop()

        else:
            playOutro()
            lives = 3
            endwindow2 = tk.Toplevel()
            endwindow2.title("You Lost!")
            endwindow2.geometry("1080x720")
            endwindow2.iconbitmap("Dice-icon.ico")
            endwindow2.resizable(False, False)
            endwindow2.configure(background="black")

            # Canvas
            canvasL2 = tk.Canvas(endwindow2, width=1080, height=720, borderwidth=0, highlightthickness=0, bg="black")
            canvasL2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            # Imagen
            jordan = Image.open("jordan.jpg")
            jordanres = jordan.resize((1080, 720), Image.ANTIALIAS)
            jordanw = ImageTk.PhotoImage(jordanres, master=canvasL2)
            jordanlisto = canvasL2.create_image(0, 0, image=jordanw, anchor=tk.NW)

            # Entry de Jugador
            entryName = tk.Entry(canvasL2)
            entryName.place(x=475, y=305)

            def savedata():
                global score
                scores = open("scores.txt", "a")
                scores.write(str(score) + " - " + str(entryName.get()) + ",")
                scores.close()
                endwindow2.destroy()
                score = 0

            # Puntuación Final
            scoreShow = tk.Label(canvasL2, text="Final Score: " + str(score), font=("Arial", "30"), bg="black",
                                 fg="white")
            scoreShow.place(x=350, y=150)

            # Titulo
            label1 = tk.Label(canvasL2, text="Enter Your Name: ", font=("Arial", 15), bg="black", fg="white")
            label1.place(x=300, y=300)

            # Botón
            botonSave = tk.Button(canvasL2, text="Save Your Stats!", command=savedata)
            botonSave.place(x=675, y=315, anchor=tk.CENTER)

            endwindow2.mainloop()

    ####################################################################################################################

    # Ventana para manejar pantalla de victoria

    def congrats():
        playIntro()
        global score
        global lives
        lives = 3
        congrats = tk.Toplevel()
        congrats.title("Congrats!")
        congrats.geometry("1080x720")
        congrats.iconbitmap("Dice-icon.ico")
        congrats.resizable(False, False)
        congrats.configure(background="black")

        ################################################################################################################

        # Canvas
        canvasEnd = tk.Canvas(congrats, width=1080, height=720, borderwidth=0, highlightthickness=0, bg="black")
        canvasEnd.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ################################################################################################################

        # Entry de Jugador
        entryName = tk.Entry(canvasEnd)
        entryName.place(x=475, y=305)

        ################################################################################################################

        def savedata():
            global score
            scores = open("scores.txt", "a")
            scores.write(str(score) + " - " + str(entryName.get()) + ",")
            scores.close()
            congrats.destroy()
            score = 0

        ################################################################################################################

        # Puntuación Final
        scoreShow = tk.Label(canvasEnd, text="Final Score: " + str(score), font=("Arial", "30"), bg="black",
                             fg="white")
        scoreShow.place(x=350, y=150)

        ################################################################################################################

        # Titulo
        label1 = tk.Label(canvasEnd, text="Enter Your Name: ", font=("Arial", 15), bg="black", fg="white")
        label1.place(x=300, y=300)
        labelA = tk.Label(canvasEnd, text="YOU MADE IT! THAT'S SO AMAZING!", font=("Arial", 25), bg="black", fg="white")
        labelA.place(x=250, y=100)

        ################################################################################################################

        # Imagen
        image = Image.open("jake.png")
        resized = image.resize((256, 256), Image.ANTIALIAS)
        nuevo = ImageTk.PhotoImage(resized, master=canvasEnd)
        produ = canvasEnd.create_image(100, 400, image=nuevo, anchor=tk.NW)

        ################################################################################################################

        # Botón
        botonSave = tk.Button(canvasEnd, text="Save Your Stats!", command=savedata)
        botonSave.place(x=675, y=315, anchor=tk.CENTER)

        congrats.mainloop()

    ####################################################################################################################

    # Ventana para Salon de la Fama
    def leaderboard():
        playIntro()
        scorewindow = tk.Toplevel()
        scorewindow.title("Hall of Death")
        scorewindow.geometry("1080x720")
        scorewindow.iconbitmap("Dice-icon.ico")
        scorewindow.resizable(False, False)
        scorewindow.configure(background="black")

        ################################################################################################################

        show = open("scores.txt", "r")
        read0 = show.read()
        read = read0.split(",")
        top = natsorted(read, reverse=True)
        print(top)
        print(read)

        ################################################################################################################

        label0 = tk.Label(scorewindow, text="TOP 3 CHALLENGERS", font=("Arial", 15), bg="black", fg="white")
        label0.place(x=450, y=100)
        label1 = tk.Label(scorewindow, text=str(top[0]), font=("Arial", 15), bg="black", fg="white")
        label1.place(x=450, y=300)
        labelA = tk.Label(scorewindow, text="1.", font=("Arial", 15), bg="black", fg="white")
        labelA.place(x=425, y=300)
        label2 = tk.Label(scorewindow, text=str(top[1]), font=("Arial", 15), bg="black", fg="white")
        label2.place(x=450, y=350)
        labelB = tk.Label(scorewindow, text="2.", font=("Arial", 15), bg="black", fg="white")
        labelB.place(x=425, y=350)
        label3 = tk.Label(scorewindow, text=str(top[2]), font=("Arial", 15), bg="black", fg="white")
        label3.place(x=450, y=400)
        labelC = tk.Label(scorewindow, text="3.", font=("Arial", 15), bg="black", fg="white")
        labelC.place(x=425, y=400)

        ################################################################################################################

        scorewindow.mainloop()

    ####################################################################################################################

    # Canvas
    canvasMenu = tk.Canvas(menuwindow, width=1080, height=720, borderwidth=0, highlightthickness=0, bg="black")
    canvasMenu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    ####################################################################################################################

    # Botones
    botonStart = tk.Button(canvasMenu, text="Start the Journey", command=startwindow)
    botonStart.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    botonScore = tk.Button(canvasMenu, text="Hall of Death", command=leaderboard)
    botonScore.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    ####################################################################################################################

    # Imágenes
    imageTotoro = Image.open("totomenu.jpg")
    resizedTotoro = imageTotoro.resize((400, 800), Image.ANTIALIAS)
    nuevoTotoro = ImageTk.PhotoImage(resizedTotoro, master=canvasMenu)
    totoro = canvasMenu.create_image(675, 50, image=nuevoTotoro, anchor=tk.NW)
    imageTitulo = Image.open("Monkey.png")
    resizedTitulo = imageTitulo.resize((916, 219), Image.ANTIALIAS)
    nuevoTitulo = ImageTk.PhotoImage(resizedTitulo, master=canvasMenu)
    titulo = canvasMenu.create_image(75, 50, image=nuevoTitulo, anchor=tk.NW)

    menuwindow.mainloop()
    ####################################################################################################################


anim.after(5000, main)  # despues de 5 segundos, llama a main(), que destruye la animacion y arranca el menu
playIntro()
anim.mainloop()
