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
global lives
lives = 3

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
    def game1():
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

        #Imagen "Dama"
        imageDama = Image.open("chi.png")
        resizedDama = imageDama.resize((75, 75), Image.ANTIALIAS)
        nuevoDama = ImageTk.PhotoImage(resizedDama, master=canvasGame)
        dama = canvasGame.create_image(225, 138, image=nuevoDama, anchor=tk.NW)


        #Platformas
        imagePlat1 = Image.open("platA.png")
        resizedPlat1 = imagePlat1.resize((1080,50), Image.ANTIALIAS)
        nuevoPlat1 = ImageTk.PhotoImage(resizedPlat1, master= canvasGame)
        plat1 = canvasGame.create_image(0, 675, image= nuevoPlat1, anchor=tk.NW)
        resizedPlat2 = imagePlat1.resize((450, 50), Image.ANTIALIAS)
        nuevoPlat2 = ImageTk.PhotoImage(resizedPlat2, master=canvasGame)
        plat2 = canvasGame.create_image(0, 475, image=nuevoPlat2, anchor=tk.NW)
        plat3 = canvasGame.create_image(700, 475, image=nuevoPlat2, anchor=tk.NW)
        plat4 = canvasGame.create_image(-179, 275, image= nuevoPlat1, anchor=tk.NW)

        #Gradas
        resizedGradA1 = imagePlat1.resize((200, 10), Image.ANTIALIAS)
        nuevoGradA1 = ImageTk.PhotoImage(resizedGradA1, master=canvasGame)
        gradaA1 = canvasGame.create_image(475, 475, image=nuevoGradA1, anchor=tk.NW)
        gradaA2 = canvasGame.create_image(475, 547, image=nuevoGradA1, anchor=tk.NW)
        gradaA3 = canvasGame.create_image(475, 610, image=nuevoGradA1, anchor=tk.NW)
        gradaB1 = canvasGame.create_image(900, 275, image=nuevoGradA1, anchor=tk.NW)
        gradaB2 = canvasGame.create_image(900, 350, image=nuevoGradA1, anchor=tk.NW)
        gradaB3 = canvasGame.create_image(900, 409, image=nuevoGradA1, anchor=tk.NW)
        resizedGradA2 = imagePlat1.resize((200, 10), Image.ANTIALIAS)
        nuevoGradA2 = ImageTk.PhotoImage(resizedGradA2, master=canvasGame)
        gradaC1 = canvasGame.create_image(250, 200, image= nuevoGradA2, anchor=tk.NW)


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
                y = 0  ## Just so it is not moved again, afterwards
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
        """
        def gravedad():
            g = .1
            x = 0
            y = -5
            while g == .1:
                canvasGame.moveto(principal, x, y)
                canvasGame.update()
                edgeReached()
                collision()
                movimiento()
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
            damacol= canvasGame.bbox(dama)
            plat1col=canvasGame.bbox(plat1)
            plat2col=canvasGame.bbox(plat2)
            plat3col=canvasGame.bbox(plat3)
            plat4col=canvasGame.bbox(plat4)
            gradaA1col=canvasGame.bbox(gradaA1)
            gradaA2col=canvasGame.bbox(gradaA2)
            gradaA3col = canvasGame.bbox(gradaA3)
            gradaB1col = canvasGame.bbox(gradaB1)
            gradaB2col = canvasGame.bbox(gradaB2)
            gradaB3col = canvasGame.bbox(gradaB3)
            gradaC1col = canvasGame.bbox(gradaC1)

            #Primera Plataforma
            global score
            if damacol[0] < princol[0] < damacol[2] and damacol[1] < princol[3] < damacol[3]:
                score += 900
                scoreShow.configure(text="SCORE: " + str(score))
                time.sleep(1.0)
                gamewindow.destroy()
            elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[0] < plat1col[2] \
                    and plat1col[0] < princol[2] < plat1col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[0] < plat1col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat1col[1] < princol[3] < plat1col[3] and plat1col[0] < princol[2] < plat1col[2]:
                canvasGame.move(principal, 0, -5)
            #Segunda Plataforma
            elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2] \
                    and plat2col[0] < princol[2] < plat2col[2]:
                score +=1
                scoreShow.configure(text="SCORE: " + str(score))
                canvasGame.move(principal, 0, -5)
            elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat2col[1] < princol[3] < plat2col[3] and plat2col[0] < princol[2] < plat2col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2] \
                    and plat2col[0] < princol[2] < plat2col[2]:
                canvasGame.move(principal, 0, 5)
            elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[0] < plat2col[2]:
                canvasGame.move(principal, 0, 5)
            elif plat2col[1] < princol[1] < plat2col[3] and plat2col[0] < princol[2] < plat2col[2]:
                canvasGame.move(principal, 0, 5)
            #Tercera Plataforma
            elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2] \
                    and plat3col[0] < princol[2] < plat3col[2]:
                score +=1
                scoreShow.configure(text="SCORE: " + str(score))
                canvasGame.move(principal, 0, -5)
            elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat3col[1] < princol[3] < plat3col[3] and plat3col[0] < princol[2] < plat3col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2] \
                    and plat3col[0] < princol[2] < plat3col[2]:
                canvasGame.move(principal, 0, 5)
            elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[0] < plat3col[2]:
                canvasGame.move(principal, 0, 5)
            elif plat3col[1] < princol[1] < plat3col[3] and plat3col[0] < princol[2] < plat3col[2]:
                canvasGame.move(principal, 0, 5)
            # Tercera Plataforma
            elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2] \
                    and plat4col[0] < princol[2] < plat4col[2]:
                score += 1
                scoreShow.configure(text="SCORE: " + str(score))
                canvasGame.move(principal, 0, -5)
            elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat4col[1] < princol[3] < plat4col[3] and plat4col[0] < princol[2] < plat4col[2]:
                canvasGame.move(principal, 0, -5)
            elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2] \
                    and plat4col[0] < princol[2] < plat4col[2]:
                canvasGame.move(principal, 0, 5)
            elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[0] < plat4col[2]:
                canvasGame.move(principal, 0, 5)
            elif plat4col[1] < princol[1] < plat4col[3] and plat4col[0] < princol[2] < plat4col[2]:
                canvasGame.move(principal, 0, 5)
            #GradaA1
            elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[0] < gradaA1col[2] \
                    and gradaA1col[0] < princol[2] < gradaA1col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[0] < gradaA1col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaA1col[1] < princol[3] < gradaA1col[3] and gradaA1col[0] < princol[2] < gradaA1col[2]:
                canvasGame.move(principal, 0, -5)
            # GradaA2
            elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[0] < gradaA2col[2] \
                    and gradaA2col[0] < princol[2] < gradaA2col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[0] < gradaA2col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaA2col[1] < princol[3] < gradaA2col[3] and gradaA2col[0] < princol[2] < gradaA2col[2]:
                canvasGame.move(principal, 0, -5)
            # GradaA3
            elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[0] < gradaA3col[2] \
                    and gradaA3col[0] < princol[2] < gradaA3col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[0] < gradaA3col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaA3col[1] < princol[3] < gradaA3col[3] and gradaA3col[0] < princol[2] < gradaA3col[2]:
                canvasGame.move(principal, 0, -5)
            # GradaB1
            elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[0] < gradaB1col[2] \
                    and gradaB1col[0] < princol[2] < gradaB1col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[0] < gradaB1col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaB1col[1] < princol[3] < gradaB1col[3] and gradaB1col[0] < princol[2] < gradaB1col[2]:
                canvasGame.move(principal, 0, -5)
            # GradaB2
            elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[0] < gradaB2col[2] \
                    and gradaB2col[0] < princol[2] < gradaB2col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[0] < gradaB2col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaB2col[1] < princol[3] < gradaB2col[3] and gradaB2col[0] < princol[2] < gradaB2col[2]:
                canvasGame.move(principal, 0, -5)
            # GradaB3
            elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[0] < gradaB3col[2] \
                    and gradaB3col[0] < princol[2] < gradaB3col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[0] < gradaB3col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaB3col[1] < princol[3] < gradaB3col[3] and gradaB3col[0] < princol[2] < gradaB3col[2]:
                canvasGame.move(principal, 0, -5)
            # GradaC1
            elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[0] < gradaC1col[2] \
                    and gradaB3col[0] < princol[2] < gradaB3col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[0] < gradaC1col[2]:
                canvasGame.move(principal, 0, -5)
            elif gradaC1col[1] < princol[3] < gradaC1col[3] and gradaC1col[0] < princol[2] < gradaC1col[2]:
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
        global score
        scoreShow = tk.Label(canvasGame, text= "SCORE: "+str(score), bg= "#072E60", fg= "white")
        scoreShow.place(x = 950, y = 25)

        #Vidas
        global lives
        livesShow = tk.Label(canvasGame, text= "LIVES: "+str(lives), bg= "black", fg="white")
        livesShow.place(x=100, y=25)
        gamewindow.mainloop()

        #Puntos que gano
        scorePlus = tk.Label(canvasGame)
    def leaderboard():
        scorewindow = tk.Toplevel()
        scorewindow.title("Hall of Death")
        scorewindow.geometry("1080x720")
        scorewindow.iconbitmap("Dice-icon.ico")
        scorewindow.resizable(False, False)
        scorewindow.configure(background="black")

        scorewindow.mainloop()

    #Botones
    botonStart=tk.Button(menuwindow, text= "Start the Journey", command=game1)
    botonStart.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    botonScore = tk.Button(menuwindow, text="Hall of Death", command=leaderboard)
    botonScore.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    #Titulos


    menuwindow.mainloop()

anim.after(1000, main)  #despues de 5 segundos, llama a main(), que destruye la animacion y arranca el menu
anim.mainloop()
