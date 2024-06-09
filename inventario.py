from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Inventario(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.widgets()

    def widgets(self):

        frame_title = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame_title.pack()
        frame_title.place(x=0, y=0, width=1100, height=100)

        title = tk.Label(self, text="INVENTARIOS", bg="#dddddd", font="sans 30 bold", anchor="center")
        title.pack()
        title.place(x=5, y=0, width=1090, height=90)

        frame_container = tk.Frame(self, bg="#d5d5d5", highlightbackground="gray", highlightthickness=1)
        frame_container.pack()
        frame_container.place(x=0, y=100, width=1100, height=550)

        lblFrameProducto = LabelFrame(frame_container, text="Productos", font="sans 16 bold", bg="#d5d5d5")
        lblFrameProducto.place(x=20, y=10, width=400, height=520)

        lblNombre = Label(lblFrameProducto, text="Nombre: ", font="sans 12 bold", bg="#d5d5d5")
        lblNombre.place(x=10, y=20)
        self.nombre = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.nombre.place(x=140, y=20, width=240)

        lblProveedor = Label(lblFrameProducto, text="Proveedor: ", font="sans 12 bold", bg="#d5d5d5")
        lblProveedor.place(x=10, y=83.75)
        self.proveedor = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.proveedor.place(x=140, y=83.75, width=240)

        lblPrecio = Label(lblFrameProducto, text="Precio: ", font="sans 12 bold", bg="#d5d5d5")
        lblPrecio.place(x=10, y=147.5)
        self.precio = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.precio.place(x=140, y=147.5, width=240)

        lblCosto = Label(lblFrameProducto, text="Costo: ", font="sans 12 bold", bg="#d5d5d5")
        lblCosto.place(x=10, y=211.25)
        self.costo = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.costo.place(x=140, y=211.25, width=240)

        lblStock = Label(lblFrameProducto, text="Stock: ", font="sans 12 bold", bg="#d5d5d5")
        lblStock.place(x=10, y=275)
        self.stock = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.stock.place(x=140, y=275, width=240)

        btnAgregar = tk.Button(lblFrameProducto, text="Agregar", bg="#0288D1", font="sans 12 bold")
        btnAgregar.place(x=80, y=340, width=240, height=50)

        btnEditar = tk.Button(lblFrameProducto, text="Editar", bg="#0288D1", font="sans 12 bold")
        btnEditar.place(x=80, y=410, width=240, height=50)

        treFrame = tk.Frame(frame_container, bg="#dddddd")
        treFrame.place(x=440, y=20, width=620, height=510)

        scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treFrame, columns=("ID", "Producto", "Proveedor", "Precio", "Costo", "Stock"), show="headings", height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)

        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Producto")
        self.tree.heading("#3", text="Proveedor")
        self.tree.heading("#4", text="Precio")
        self.tree.heading("#5", text="Costo")
        self.tree.heading("#6", text="Stock")

        self.tree.column("ID", anchor="center")
        self.tree.column("Producto", anchor="center")
        self.tree.column("Proveedor", anchor="center")
        self.tree.column("Precio", anchor="center")
        self.tree.column("Costo", anchor="center")
        self.tree.column("Stock", anchor="center")

        self.tree.pack(expand=True, fill=BOTH)


