from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Ventas(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        
        frame_title = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame_title.pack()
        frame_title.place(x=0, y=0, width=1100, height=100)

        title = tk.Label(self, text="VENTAS", bg="#dddddd", font="sans 30 bold", anchor="center")
        title.pack()
        title.place(x=5, y=0, width=1090, height=90)

        frame_container = tk.Frame(self, bg="#d5d5d5", highlightbackground="gray", highlightthickness=1)
        frame_container.pack()
        frame_container.place(x=0, y=100, width=1100, height=550)

        lblFrameInfFactura = LabelFrame(frame_container, text="Informacion de Ventas", bg="#d5d5d5", font="sans 16 bold")
        lblFrameInfFactura.place(x=10, y=10, width=1078, height=80)

        lblNroFactura = tk.Label(lblFrameInfFactura, text="Nro. de Factura: ", bg="#d5d5d5", font="sans 12 bold")
        lblNroFactura.place(x=10, y=10)
        self.nroFactura = tk.StringVar()

        self.entryNroFactura = ttk.Entry(lblFrameInfFactura, textvariable=self.nroFactura, state="reandoly", font="sans 12 bold", justify="right")
        self.entryNroFactura.place(x=143, y=11, width=100)

        lblProducto = tk.Label(lblFrameInfFactura, text="Producto: ", bg="#d5d5d5", font="sans 12 bold")
        lblProducto.place(x=250, y=10)
        self.entryProducto = ttk.Entry(lblFrameInfFactura, font="sans 12 bold")
        self.entryProducto.place(x=340, y=11, width=180)

        lblPrecio = tk.Label(lblFrameInfFactura, text="Precio: ", bg="#d5d5d5", font="sans 12 bold")
        lblPrecio.place(x=525, y=10)
        self.entryPrecio = ttk.Entry(lblFrameInfFactura, font="sans 12 bold")
        self.entryPrecio.place(x=590, y=11, width=180)

        lblCantidad = tk.Label(lblFrameInfFactura, text="Cantidad: ", bg="#d5d5d5", font="sans 12 bold")
        lblCantidad.place(x=775, y=10)
        self.entryCantidad = ttk.Entry(lblFrameInfFactura, font="sans 12 bold")
        self.entryCantidad.place(x=860, y=11, width=180)

        treFrame = tk.Frame(frame_container, bg="#dddddd")
        treFrame.place(x=150, y=120, width=800, height=200)

        scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treFrame, columns=("Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)

        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Precio")
        self.tree.heading("#3", text="Cantidad")
        self.tree.heading("#4", text="Subtotal")

        self.tree.column("Producto", anchor="center")
        self.tree.column("Precio", anchor="center")
        self.tree.column("Cantidad", anchor="center")
        self.tree.column("Subtotal", anchor="center")

        self.tree.pack(expand=True, fill=BOTH)

        lblFrameOpciones = LabelFrame(frame_container, text="Opciones", bg="#d5d5d5", font="sans 16 bold")
        lblFrameOpciones.place(x=10, y=380, width=1078, height=100)

        btnAgregar = tk.Button(lblFrameOpciones, text="Agregar", bg="#0288D1", font="sans 12 bold")
        btnAgregar.place(x=50, y=10, width=240, height=50)

        btnPagar = tk.Button(lblFrameOpciones, text="Pagar", bg="#0288D1", font="sans 12 bold")
        btnPagar.place(x=400, y=10, width=240, height=50)

        btnVer = tk.Button(lblFrameOpciones, text="Ver", bg="#0288D1", font="sans 12 bold")
        btnVer.place(x=750, y=10, width=240, height=50)

