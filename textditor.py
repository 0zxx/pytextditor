import tkinter as tk
import logging
logging.basicConfig(level=logging.CRITICAL)
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("TextEditor")

        self.text = tk.Text(master)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(master)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        self.open_button = tk.Button(master, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.RIGHT)

        self.save_button = tk.Button(master, text="Save", command=self.save)
        self.save_button.pack(side=tk.LEFT)

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.pack(side=tk.TOP)

        self.search_entry = tk.Entry(master)
        self.search_entry.pack(side=tk.TOP)

        self.search_button = tk.Button(master, text="Search", command=self.search)
        self.search_button.pack(side=tk.TOP)

        self.replace_label = tk.Label(master, text="Replace:")
        self.replace_label.pack(side=tk.TOP)

        self.replace_entry = tk.Entry(master)
        self.replace_entry.pack(side=tk.TOP)

        self.replace_button = tk.Button(master, text="Replace", command=self.replace)
        self.replace_button.pack(side=tk.TOP)

        self.text.bind("<Control-a>", self.select_all)

    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        with open(file_path, 'w') as file:
            file.write(self.text.get('1.0', tk.END))

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text.delete('1.0', tk.END)
                self.text.insert('1.0', file.read())

    def select_all(self, event):
        self.text.tag_add(tk.SEL, '1.0', tk.END)
        return 'break'

    def search(self):
        search_string = self.search_entry.get()
        if search_string:
            start = '1.0'
            while True:
                start = self.text.search(search_string, start, tk.END)
                if not start:
                    break
                end = f"{start}+{len(search_string)}c"
                self.text.tag_add("highlight", start, end)
                start = end

    def replace(self):
        search_string = self.search_entry.get()
        replace_string = self.replace_entry.get()
        if search_string and replace_string:
            content = self.text.get('1.0', tk.END)
            new_content = content.replace(search_string, replace_string)
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', new_content)

root = tk.Tk()
editor = TextEditor(root)
root.mainloop()

