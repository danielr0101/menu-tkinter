import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Inventario(tk.Frame):

    db_name = "database.db"

    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
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
        self.nombre.place(x=140, y=16, width=240)

        lblProveedor = Label(lblFrameProducto, text="Proveedor: ", font="sans 12 bold", bg="#d5d5d5")
        lblProveedor.place(x=10, y=83.75)
        self.proveedor = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.proveedor.place(x=140, y=79.75, width=240)

        lblPrecio = Label(lblFrameProducto, text="Precio: ", font="sans 12 bold", bg="#d5d5d5")
        lblPrecio.place(x=10, y=147.5)
        self.precio = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.precio.place(x=140, y=143.5, width=240)

        lblCosto = Label(lblFrameProducto, text="Costo: ", font="sans 12 bold", bg="#d5d5d5")
        lblCosto.place(x=10, y=211.25)
        self.costo = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.costo.place(x=140, y=207.25, width=240)

        lblStock = Label(lblFrameProducto, text="Stock: ", font="sans 12 bold", bg="#d5d5d5")
        lblStock.place(x=10, y=275)
        self.stock = ttk.Entry(lblFrameProducto, font="sans 12 bold")
        self.stock.place(x=140, y=271, width=240)

        btnAgregar = tk.Button(lblFrameProducto, text="Agregar", bg="#0288D1", font="sans 12 bold", command=self.registrar)
        btnAgregar.place(x=80, y=340, width=240, height=50)

        btnEditar = tk.Button(lblFrameProducto, text="Editar", bg="#0288D1", font="sans 12 bold", command=self.editar_producto)
        btnEditar.place(x=80, y=410, width=240, height=50)

        treFrame = tk.Frame(frame_container, bg="#dddddd")
        treFrame.place(x=440, y=20, width=620, height=430)

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

        self.tree.column("ID", width=70, anchor="center")
        self.tree.column("Producto", width=100, anchor="center")
        self.tree.column("Proveedor", width=100, anchor="center")
        self.tree.column("Precio", width=100, anchor="center")
        self.tree.column("Costo", width=100, anchor="center")
        self.tree.column("Stock", width=70, anchor="center")


        self.tree.pack(expand=True, fill=BOTH)


        self.mostrar()

        btn_actualizar = Button(frame_container, text="Actualizar Inventario", font="sans 14 bold", command=self.actualizar_inventario)
        btn_actualizar.place(x=440, y=480, width=260, height=50)


    def eje_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(consulta, parametros)
            conn.commit()
        return result
    
    def validacion(self, nombre, prov, precio, costo, stock):
        if not (nombre and prov and precio and costo and stock):
            return False
        try:
            float(precio)
            float(costo)
            int(stock)
        except ValueError:
            return False
        return True
    
    def mostrar(self):
        consulta = "SELECT * FROM inventario ORDER BY id DESC"
        result = self.eje_consulta(consulta)
        for elem in result:
            try:
                precio = "${:,.2f}".format(float(elem[3])) if elem[3] else ""
                costo = "${:,.2f}".format(float(elem[4])) if elem[4] else ""
            except ValueError:
                precio = elem[3]
                costo = elem[4]
            self.tree.insert("", 0, text=elem[0], values=(elem[0], elem[1], elem[2], precio, costo, elem[5]))
    
    def actualizar_inventario(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.mostrar()

        messagebox.showinfo("Actualizacion", "El inventario a sido actualizado correctamente.")

    def registrar(self):
        result = self.tree.get_children()
        for i in result:
            self.tree.delete(i)
        nombre = self.nombre.get()
        prov = self.proveedor.get()
        precio = self.precio.get()
        costo = self.costo.get()
        stock = self.stock.get()
        if self.validacion(nombre, prov, precio, costo, stock):
            try:
                consulta = "INSERT INTO inventario VALUES (?,?,?,?,?,?)"
                parametros = (None, nombre, prov, precio, costo, stock)
                self.eje_consulta(consulta, parametros)
                self.mostrar()
                self.nombre.delete(0, END)
                self.proveedor.delete(0, END)
                self.precio.delete(0, END)
                self.costo.delete(0, END)
                self.stock.delete(0, END)
            except Exception as e:
                messagebox.showwarning(title="Error", message=f"Error al registrar el producto: {e}")
        else:
            messagebox.showwarning(title="Error", message="Rellene todos los campos correctamente")
            self.mostrar()

    def editar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Editar Producto", "Seleccione un producto para editar.")
            return
    
        item_id = self.tree.item(seleccion)["text"]
        item_values = self.tree.item(seleccion)["values"]

        ventana_editar = Toplevel(self)
        ventana_editar.title("Editar Producto")        
        window_width = 400
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        ventana_editar.geometry(f"{window_width}x{window_height}+{x}+{y}")
        ventana_editar.config(bg="#d5d5d5")

        lblNombre = Label(ventana_editar, text="Nombre:", font="sans 14 bold", bg="#d5d5d5")
        lblNombre.grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = Entry(ventana_editar, font="sans 14 bold")
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_nombre.insert(0, item_values[1])

        lblProveedor = Label(ventana_editar, text="Proveedor:", font="sans 14 bold", bg="#d5d5d5")
        lblProveedor.grid(row=1, column=0, padx=10, pady=10)
        entry_proveedor = Entry(ventana_editar, font="sans 14 bold")
        entry_proveedor.grid(row=1, column=1, padx=10, pady=10)
        entry_proveedor.insert(0, item_values[2])

        lblPrecio = Label(ventana_editar, text="Precio:", font="sans 14 bold", bg="#d5d5d5")
        lblPrecio.grid(row=2, column=0, padx=10, pady=10)
        entry_precio = Entry(ventana_editar, font="sans 14 bold")
        entry_precio.grid(row=2, column=1, padx=10, pady=10)
        entry_precio.insert(0, item_values[3].split()[0].replace(",", ""))

        lblCosto = Label(ventana_editar, text="Costo:", font="sans 14 bold", bg="#d5d5d5")
        lblCosto.grid(row=3, column=0, padx=10, pady=10)
        entry_costo = Entry(ventana_editar, font="sans 14 bold")
        entry_costo.grid(row=3, column=1, padx=10, pady=10)
        entry_costo.insert(0, item_values[4].split()[0].replace(",", ""))

        lblStock = Label(ventana_editar, text="Stock:", font="sans 14 bold", bg="#d5d5d5")
        lblStock.grid(row=4, column=0, padx=10, pady=10)
        entry_stock = Entry(ventana_editar, font="sans 14 bold")
        entry_stock.grid(row=4, column=1, padx=10, pady=10)
        entry_stock.insert(0, item_values[5])

        def guardar_cambios():
            nombre = entry_nombre.get()
            proveedor = entry_proveedor.get()
            precio = entry_precio.get()
            costo = entry_costo.get()
            stock = entry_stock.get()

            if not (nombre and proveedor and precio and costo and stock):
                messagebox.showwarning("Guardar cambios", "Rellene todo los campos.")
                return
            
            try:
                precio = float(precio.replace(",", ""))
                costo = float(costo.replace(",", ""))
            except ValueError:
                messagebox.showwarning("Guardar cambios", "Ingrese valores numéricos válidos para precio y costo.")
                return
            
            consulta = "UPDATE inventario SET nombre=?, proveedor=?, precio=?, costo=?, stock=? WHERE id=?"
            parametros = (nombre,proveedor,precio,costo,stock, item_id)
            self.eje_consulta(consulta, parametros)

            self.actualizar_inventario()

            ventana_editar.destroy()

        btnGuardar = Button(ventana_editar, text="Guardar Cambios", font="sans 14 bold", command=guardar_cambios)
        btnGuardar.place(x=80, y=250, width=240, height=40)

