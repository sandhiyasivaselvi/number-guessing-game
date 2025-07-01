import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.random_number = random.randint(1, 100)
        self.attempts = 10

        self.label = tk.Label(root, text="Guess a number between 1 and 100")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.check_button = tk.Button(root, text="Check", command=self.check_guess)
        self.check_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.message_label = tk.Label(root, text="")
        self.message_label.pack()

        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.attempts}")
        self.attempts_label.pack()

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.message_label.config(text="Enter a valid number.")
            return

        guess = int(guess)
        self.attempts -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

        if guess == self.random_number:
            self.message_label.config(text="Congratulations! You guessed it right!")
        elif guess < self.random_number:
            self.message_label.config(text="Too low!")
        else:
            self.message_label.config(text="Too high!")

        if self.attempts == 0 and guess != self.random_number:
            self.message_label.config(text=f"Game Over! The number was {self.random_number}.")

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 10
        self.entry.delete(0, tk.END)
        self.message_label.config(text="")
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

# Run the GUI game
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
