import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.max_attempts = 10
        self.attempts = 0
        self.secret_number = random.randint(1, 100)

        # Create and configure GUI elements
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="Number Guessing Game",
            font=("Helvetica", 20, "bold"),
            bg="#f0f0f0",
            pady=20
        )
        title_label.pack()

        # Instructions
        instructions = "Guess a number between 1 and 100"
        self.instruction_label = tk.Label(
            self.root,
            text=instructions,
            font=("Helvetica", 12),
            bg="#f0f0f0",
            pady=10
        )
        self.instruction_label.pack()

        # Entry field
        self.guess_entry = tk.Entry(
            self.root,
            font=("Helvetica", 14),
            width=10,
            justify='center'
        )
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind('<Return>', lambda e: self.check_guess())

        # Submit button
        submit_button = tk.Button(
            self.root,
            text="Submit Guess",
            command=self.check_guess,
            font=("Helvetica", 12),
            bg="#4CAF50",
            fg="white",
            pady=5
        )
        submit_button.pack(pady=10)

        # Feedback label
        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 12),
            bg="#f0f0f0",
            wraplength=350
        )
        self.feedback_label.pack(pady=10)

        # Attempts label
        self.attempts_label = tk.Label(
            self.root,
            text="Attempts remaining: 10",
            font=("Helvetica", 12),
            bg="#f0f0f0"
        )
        self.attempts_label.pack(pady=10)

        # New Game button
        new_game_button = tk.Button(
            self.root,
            text="New Game",
            command=self.reset_game,
            font=("Helvetica", 12),
            bg="#2196F3",
            fg="white",
            pady=5
        )
        new_game_button.pack(pady=10)

        # Quit button
        quit_button = tk.Button(
            self.root,
            text="Quit",
            command=self.root.quit,
            font=("Helvetica", 12),
            bg="#f44336",
            fg="white",
            pady=5
        )
        quit_button.pack(pady=10)

    def check_guess(self):
        # Get the guess from the entry field
        try:
            guess = int(self.guess_entry.get())
            if not 1 <= guess <= 100:
                self.feedback_label.config(
                    text="Please enter a number between 1 and 100",
                    fg="red"
                )
                return
        except ValueError:
            self.feedback_label.config(
                text="Please enter a valid number",
                fg="red"
            )
            return

        self.attempts += 1
        remaining = self.max_attempts - self.attempts

        # Check the guess
        if guess == self.secret_number:
            messagebox.showinfo(
                "Congratulations!",
                f"You've won! You guessed the number in {self.attempts} attempts!"
            )
            self.reset_game()
        elif self.attempts >= self.max_attempts:
            messagebox.showinfo(
                "Game Over",
                f"Sorry, you've run out of attempts. The number was {self.secret_number}"
            )
            self.reset_game()
        else:
            if guess < self.secret_number:
                feedback = "Too low! Try a higher number."
                color = "blue"
            else:
                feedback = "Too high! Try a lower number."
                color = "orange"
            
            self.feedback_label.config(text=feedback, fg=color)
            self.attempts_label.config(text=f"Attempts remaining: {remaining}")

        # Clear the entry field
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="", fg="black")
        self.attempts_label.config(text="Attempts remaining: 10")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()