import tkinter as tk
import random as ran
from tkinter import messagebox
import string#ascii

window = tk.Tk()

window.geometry("750x550")
window.title("Wordle Game")
window.configure(bg="light gray")


class WordleGame:

  def __init__(self, window):
    self.window = window
    self.word_list = self.load_words("words.txt")
    self.attempts = 0
    self.current_word = ran.choice(self.word_list)
    self.word_length = len(self.current_word)
    self.guesses = self.Guesses()
    self.labels = self.LoadLabels()
    self.entry = tk.Entry(window, width=15, font=("Arial", 20))
    self.entry.grid(row=7, column=0, columnspan=50, padx=5, pady=6)
    self.submit = tk.Button(window, text="Submit", command=self.CheckGuess)
    self.submit.grid(row=8, column=0, columnspan=50, padx=5, pady=6)
    #print(self.current_word)

  def Guesses(self):
    return [[" " for _ in range(5)] for _ in range(6)]

  def LoadLabels(self):
    labels = [[tk.Label(window, text="", width=5, height=3) for _ in range(5)]
              for _ in range(6)]
    for rows in range(6):
      for c in range(5):
        labels[rows][c].grid(row=rows + 1, column=c, padx=3, pady=4)
    return labels

  def load_words(self, filename):
    with open(filename, "r") as file:
      return [line.strip() for line in file.readlines()]

  def update_labels(self):
    global Keyboard_Dictionary
    guess_letter = ""
    correct_letter = ""
    correct_counter = 0
    for i in range(self.attempts):
      correct_counter = 0
      for j in range(5):
        guess_letter = self.guesses[i][j].upper()
        correct_letter = self.current_word[j].upper()
        self.labels[i][j].config(text=guess_letter)

        # print("Guessed letter" ,guess_letter)#needs to be lowercase
        # print("Current Word" , self.current_word)

        if guess_letter == correct_letter:
          self.labels[i][j].config(bg="green", fg="blue")
          Keyboard_Dictionary[guess_letter.lower()] = "green"
          self.make_keyboard()
          correct_counter += 1
        elif guess_letter.lower() in self.current_word:
          self.labels[i][j].config(bg="yellow", fg="black")
          Keyboard_Dictionary[guess_letter.lower()] = "yellow"
          self.make_keyboard()
          #print("yellow")
        else:
          if guess_letter != "":
            self.labels[i][j].config(bg="red", fg="white")
            Keyboard_Dictionary[guess_letter.lower()] = "red"
            self.make_keyboard()
          else:
            self.labels[i][j].config(bg="white", fg="black")
    if correct_counter == 5:
      self.display("You got it right!" + self.current_word)
      self.entry.config(state= tk.DISABLED)
      self.submit.config(state= tk.DISABLED)
    if self.attempts >= 6:
      self.display("You ran out of attempts, You lose!" + self.current_word)
      self.entry.config(state= tk.DISABLED)
      self.submit.config(state= tk.DISABLED)

  def display(self, message):
    messagebox.showinfo("Message", message)

  def CheckGuess(self):
    global Keyboard_Dictionary
    print(Keyboard_Dictionary)
    guess = self.entry.get().strip().lower()
    print(guess)
    print(self.word_length)
    if len(guess) == self.word_length:
      if self.attempts < 6:
        self.guesses[self.attempts] = list(guess)  #turns guess into array
        self.attempts += 1
        self.update_labels()
        self.entry.delete(0, tk.END)

      else:
        self.display("You Lost! The Word was " + self.current_word)
        self.entry.config(state=tk.DISABLED)
        self.submit.config(state=tk.DISABLED)
    else:
      self.entry.delete(0, tk.END)

  def letter_template(self,letter,colour, xpos , ypos):
    Letter_Label = tk.Label(self.window,text=letter,bg=colour,width= 4,height = 2)
    Letter_Label.place(x = xpos, y = ypos)
  
 


  #new 12th March
  def keyboard(self):
    global Keyboard_Dictionary
    self.keyboard_rows = [
      "qwertyuiop",
      "asdfghjkl",
      "zxcvbnm"
    ]
    Keyboard_Dictionary = {}
    #nested loop that will cycle through each row in the dictionary and get wach letter
    for row in self.keyboard_rows:
      for letter in row:
        Keyboard_Dictionary[letter] = "gray"

    print(Keyboard_Dictionary)



  def make_keyboard(self):
    global Keyboard_Dictionary
    print("Update keybaord")
    startx = 300
    starty = 200
    x_change = 40
    y_change = 40
    for index,row in enumerate(self.keyboard_rows):
      CurentX = startx
      CurentY = starty + (index * y_change)
      if index == 1:
        CurentX += x_change /2
      elif index == 2:
        CurentX += x_change
      for letter in row:
        Colour = Keyboard_Dictionary[letter]
        self.letter_template(letter,Colour,CurentX, CurentY)
        CurentX += x_change
  

 







game = WordleGame(window)
stuff = game.load_words("words.txt")
#print(stuff)
game.keyboard()
# game.letter_template("q", "grey",400,400)
# game.letter_template("w","red",300,300)
game.make_keyboard()

#To Do Next
#Pop up to ask if you want to play agin
#Restart
#Delete old make keyboards


window.mainloop()
