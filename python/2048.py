import random
import pygame
import time
import tkinter as tk
from array import *
width = 350
height = 450


window = tk.Tk()

window.geometry(f"{width}x{height}")
window.configure(bg = "#b7a4c5")
window.title("2048 by Aayana")
rows = 4
cols = 4

#squares = [[0]* cols]* rows
squares = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]




class Game2048:
    def __init__(self):
        self.window = window
        self.label = self.makeLabels()
    def makeLabels(self):
        global labels
        startx = 0
        starty = 0
        labels = [[tk.Label(window, text = "", width = 9, height = 6) for i in range(4)]for j in range(4)]
        for i in range(4):
            for j in range(4):
                labels[i][j].grid(row = i+1,column = j, padx = 5, pady=5)
        return labels

    def GetNumber(self):
        numbers = [ 2 , 4]
        newnum = random.choice(numbers)
        return newnum

    def PlaceNumber(self):
        row = random.randint(1,4)
        column = random.randint(1,4)
        number = self.GetNumber()
        print("Number = ", number, "row: ", row, "column: ", column)
        #squares[1][1] = number
        squares[row-1][column-1] = number
        print(squares)
        self.UpdateBox(number, row, column)

    def UpdateBox(self, number, row, column):
      labels[row-1][column-1].config(text=number)
      print("Update")

    
    
    






Game = Game2048()
Game.makeLabels()
Game.PlaceNumber()
window.mainloop()
