from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario

class Container(tk.Frame):
    def __init__(self, padre, controller):
        super().__init__(padre)
        self.controller = controller
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#D5D5D5")
        self.widgets()

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#D5D5D5")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)

    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        self.show_frames(Inventario)

    def widgets(self):

        frame1 = tk.Frame(self, bg="#D5D5D5")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)

        btnVentas = Button(frame1, bg="green", fg="black", text="Ventas", command=self.ventas)
        btnVentas.place(x=500, y=30, width=240, height=60)

        btnInventario = Button(frame1, bg="blue", fg="white", text="Inventario", command=self.inventario)
        btnInventario.place(x=500, y=130, width=240, height=60)