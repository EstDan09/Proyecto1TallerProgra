import tkinter as tk
from PIL import ImageTk, Image
import shelve
import pygame
import random
import time
from threading import Thread
def test():
    endwindow1 = tk.Tk()
    endwindow1.title("You Lost!")
    endwindow1.geometry("1080x720")
    endwindow1.iconbitmap("Dice-icon.ico")
    endwindow1.resizable(False, False)
    endwindow1.configure(background="black")

    # Entry de Jugador
    entryName = tk.Entry(endwindow1)
    entryName.place(x=475, y=305)

    #def savedata():



    #Puntuacion Final
    scoreShow = tk.Label(endwindow1, text="Final Score: ",font=("Arial", "30"), bg="black", fg="white")
    scoreShow.place(x=350, y=150)

    #Titulo
    label1 = tk.Label(endwindow1, text="Enter Your Name: ", font=("Arial", 15), bg="black", fg="white")
    label1.place(x=300, y= 300)

    #Boton
    botonSave = tk.Button(endwindow1, text="Save Your Stats!")
    botonSave.place(x=675, y=315, anchor=tk.CENTER)

    endwindow1.mainloop()

test()