import tkinter as tk
import logging
logging.basicConfig(level=logging.CRITICAL)
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("TextEditor")

        # Create a frame to hold the Text widget and line number Text widget
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the Text widget and scrollbar
        self.text = tk.Text(frame)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        scroll = tk.Scrollbar(frame, command=self.text.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=scroll.set)

        # Create the line number Text widget
        self.line_numbers = tk.Text(frame, width=4, padx=5, pady=5, takefocus=0, border=0, background='lightgray', state='disabled')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Bind the Text widget to update the line numbers
        self.text.bind('<<Modified>>', self.update_line_numbers)
        self.text.bind('<Configure>', self.update_line_numbers)
        self.text.bind('<Return>', self.refresh_text)

        self.save_button = tk.Button(master, text="Save", command=self.save)
        self.save_button.pack()

    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        with open(file_path, 'w') as file:
            file.write(self.text.get('1.0', tk.END))

    def update_line_numbers(self, event=None):
        """Update the line numbers in the line_numbers Text widget"""
        # Clear the line_numbers widget
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', tk.END)

        # Get the number of lines in the text widget
        num_lines = str(self.text.count('1.0', tk.END, 'displaylines')[0])

        # Add the line numbers to the line_numbers widget
        for i in range(1, int(num_lines) + 1):
            self.line_numbers.insert(tk.END, str(i) + '\n')

        # Disable the line_numbers widget
        self.line_numbers.config(state='disabled')

    def refresh_text(self, event=None):
        """Refresh the text in the Text widget"""
        self.update_line_numbers()
        self.text.update()

root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
