import tkinter as tk
from .labelentry import LabelEntry


class SizeEntrySet(tk.Frame):
    def __init__(self, master, width_text=None, height_text=None):
        super().__init__(master)

        self.width_entry = LabelEntry(self, text=width_text)
        self.width_entry.pack(side=tk.LEFT)

        self.height_entry = LabelEntry(self, text=height_text)
        self.height_entry.pack(side=tk.LEFT)

    def get_width_text(self):
        return self.width_entry.get()

    def get_height_text(self):
        return self.height_entry.get()

