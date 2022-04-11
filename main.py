#Librerias
import tkinter as tk
from PIL import ImageTk, Image
import pygame
import random
import time
from threading import Thread

#Puntuacion
score = 0
jump_counter = 0
fall = True

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
        principal = canvasGame.create_image(125, 600, image=nuevoPrin, anchor=tk.NW)

        #Platformas
        imagePlat1 = Image.open("platA.png")
        resizedPlat1 = imagePlat1.resize((1080,50), Image.ANTIALIAS)
        nuevoPlat1 = ImageTk.PhotoImage(resizedPlat1, master= canvasGame)
        plat1 = canvasGame.create_image(0, 675, image= nuevoPlat1, anchor=tk.NW)
        resizedPlat2 = imagePlat1.resize((400, 50), Image.ANTIALIAS)
        nuevoPlat2 = ImageTk.PhotoImage(resizedPlat2, master=canvasGame)
        plat2 = canvasGame.create_image(50, 475, image=nuevoPlat2, anchor=tk.NW)
        plat3 = canvasGame.create_image(600, 475, image=nuevoPlat2, anchor=tk.NW)

        #Movimiento
        def movimiento():
            def left(event):
                x = -5
                y = 0
                edgeReached()
                canvasGame.move(principal,x, y)
                collision()

            def right(event):
                x = 5
                y = 0
                edgeReached()
                canvasGame.move(principal,x, y)
                collision()

            def jump(event):
                x = 0
                diff = 0  ## Difference to initial level
                y = -4  ## Initial speed in y direction
                grav = .1  ## Gravitation

                while diff >= 0:  ## While it is still jumping (higher than initially)
                    canvasGame.move(principal, x, y)
                    canvasGame.update()
                    time.sleep(.01)  ## Pause for 1/100 second
                    diff -= y  ## Update current jumping height
                    y += grav  ## Update the speed in y direction
                y = 0  ## Just so it is not moved again, afterwards
                edgeReached()
                canvasGame.move(principal, x, y)
                collision()

            def climb(event):
                x = 0
                y = 5
                edgeReached()
                canvasGame.move(principal,x, y)
                collision()

            def gravity():
                pri = canvasGame.bbox(principal)
                prim = canvasGame.bbox(plat1)
                seg = canvasGame.bbox(plat2)
                ter = canvasGame.bbox(plat3)
                while not (prim[1] < pri[3] < prim[3] and prim[0] < pri[0] < prim[2] and prim[0] < pri[2] < prim[2]):
                    def gravedad():
                        g = .1
                        x = 0
                        y = -5
                        while g == .1:
                            canvasGame.moveto(principal, x, y)
                            canvasGame.update()
                            y += g
                        edgeReached()
                        canvasGame.move(principal, x, y)
                        collision()

                    gravedad()



            canvasGame.bind_all("<Left>", left)
            canvasGame.bind_all("<Right>", right)
            canvasGame.bind_all("<Up>", jump)
            canvasGame.bind_all("<Down>", climb)
        movimiento()
        """
        def gravedad():
            g = .1
            x = 0
            y = -5
            while g == .1:
                canvasGame.moveto(principal, x, y)
                canvasGame.update()
                y += g
            edgeReached()
            canvasGame.move(principal,x, y)
            collision()
        gravedad()
        """
        #Controles
        #canvasGame.bind_all("<Enter>", start)


        #Colisiones
        def collision():
            princol= canvasGame.bbox(principal)
            plat1col=canvasGame.bbox(plat1)
            plat2col=canvasGame.bbox(plat2)
            plat3col=canvasGame.bbox(plat3)
            #Primera Plataforma
            global score
            if plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[0] < plat1col[2] \
                    and plat1col[0] < princol[2] < plat1col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[0] < plat1col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[2] < plat1col[2]:
                canvasGame.move(principal, 0, -5)
            #Segunda Plataforma
            elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2] \
                    and plat2col[0] < princol[2] < plat2col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[2] < plat2col[2]:
                canvasGame.move(principal, 0, -5)



        #Pesonaje no se salga de la ventana
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
                canvasGame.move(principal, 0, 10)
            elif prinbottom > 720:
                canvasGame.move(principal, 0, -10)


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
