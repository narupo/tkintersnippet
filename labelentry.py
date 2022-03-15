import tkinter as tk


class LabelEntry(tk.Frame):
    def __init__(self, master, text=None):
        super().__init__(master)

        self.label = tk.Label(self, text=text)
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.RIGHT)

    def get(self):
        return self.entry.get()
