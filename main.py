
# main.py

import tkinter as tk
from tkinter import scrolledtext
import textwrap
from game_data import challenges
from utils import run_code

class CodeQuestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Quest Adventure")
        self.challenge_index = 0

        # Create widgets
        self.create_widgets()
        self.load_challenge()

    def create_widgets(self):
        # Create and pack the text area for code input
        self.code_editor = scrolledtext.ScrolledText(self.root, width=80, height=20, wrap=tk.WORD)
        self.code_editor.pack(padx=10, pady=10)

        # Create and pack the submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_code)
        self.submit_button.pack(pady=5)

        # Create and pack the challenge label
        self.challenge_label = tk.Label(self.root, text="", wraplength=600)
        self.challenge_label.pack(pady=10)

        # Create and pack the result label
        self.result_label = tk.Label(self.root, text="", wraplength=600)
        self.result_label.pack(pady=10)

        # Create and pack the hint label
        self.hint_label = tk.Label(self.root, text="", wraplength=600, fg="blue")
        self.hint_label.pack(pady=10)

    def load_challenge(self):
        """Loads the current challenge and displays it."""
        if self.challenge_index < len(challenges):
            challenge = challenges[self.challenge_index]
            self.challenge_label.config(text="Challenge:\n" + textwrap.fill(challenge["question"], width=80))
            self.result_label.config(text="")
            self.hint_label.config(text="")
            self.code_editor.delete(1.0, tk.END)  # Clear the editor
        else:
            self.challenge_label.config(text="Congratulations! You've completed all challenges.")
            self.submit_button.config(state=tk.DISABLED)

    def submit_code(self):
        """Handles code submission and validation."""
        user_code = self.code_editor.get(1.0, tk.END).strip()
        challenge = challenges[self.challenge_index]
        result = run_code(user_code)
        
        if "Error" in result:
            self.result_label.config(text=result)
            self.hint_label.config(text=f"Hint: {challenge['hint']}")
        else:
            self.result_label.config(text="Well done! You've completed this challenge.")
            self.challenge_index += 1
            self.load_challenge()

def main():
    """Main function to start the game."""
    root = tk.Tk()
    app = CodeQuestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
