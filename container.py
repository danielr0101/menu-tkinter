from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controller):
        super().__init__(padre)
        self.controller = controller
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#D5D5D5")
        self.widgets()

    def show_frames(self, container, title):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#D5D5D5")
        frame.pack(fill="both", expand=True)    
        window_width = 1100
        window_height = 650
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        top_level.geometry(f"{window_width}x{window_height}+{x}+{y}")
        top_level.resizable(False, False)

        top_level.transient(self.master)  
        top_level.grab_set()  
        top_level.focus_set()  
        top_level.lift()

        top_level.title(title)

    def ventas(self):
        self.show_frames(Ventas,"Ventas")

    def inventario(self):
        self.show_frames(Inventario, "Inventario")

    def widgets(self):

        frame1 = tk.Frame(self, bg="#D5D5D5")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)

        imagen_pil = Image.open("iconos/btn-ventas.png")
        imagen_resize = imagen_pil.resize((50, 50))
        imagen_tk = ImageTk.PhotoImage(imagen_resize)

        btnVentas = Button(frame1, bg="#0288D1", fg="black", text="Ventas", font= "sans 18 bold", command=self.ventas)
        btnVentas.config(image=imagen_tk, compound=LEFT, padx=55)
        btnVentas.image = imagen_tk
        btnVentas.place(x=500, y=30, width=240, height=60)

        imagen_pil = Image.open("iconos/btn-inventario.png")
        imagen_resize = imagen_pil.resize((50, 50))
        imagen_tk = ImageTk.PhotoImage(imagen_resize)

        btnInventario = Button(frame1, bg="#0288D1", fg="black", text="Inventario", font= "sans 18 bold", command=self.inventario)
        btnInventario.config(image=imagen_tk, compound=LEFT, padx=25)
        btnInventario.image = imagen_tk
        btnInventario.place(x=500, y=130, width=240, height=60)

        self.logo_image = Image.open("images/logo.png")
        self.logo_image = self.logo_image.resize((280, 280))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#D5D5D5")
        self.logo_label.place(x=100, y=30)

        copyright_label = tk.Label(frame1, text="© 2024 Ariona Devs. Todos los derechos reservados.", font= "sans 12 bold", bg="#D5D5D5", fg="gray")
        copyright_label.place(x=190, y=350)