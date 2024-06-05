from tkinter import *
import tkinter as tk

class Container(tk.Frame):
    def __init__(self, padre, controller):
        super().__init__(padre)
        self.controller = controller
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#D5D5D5")