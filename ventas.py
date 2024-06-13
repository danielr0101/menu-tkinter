import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Ventas(tk.Frame):

    db_name = "database.db"

    def __init__(self, parent):
        super().__init__(parent)
        self.numero_factura_actual = self.obtener_numero_factura_actual()
        self.widgets()
        self.mostrar_numero_factura()

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

        self.entryNroFactura = ttk.Entry(lblFrameInfFactura, textvariable=self.nroFactura, state="readonly", font="sans 12 bold", justify="right")
        self.entryNroFactura.place(x=143, y=7, width=100)

        lblProducto = tk.Label(lblFrameInfFactura, text="Producto: ", bg="#d5d5d5", font="sans 12 bold")
        lblProducto.place(x=250, y=10)
        self.entryProducto = ttk.Combobox(lblFrameInfFactura, font="sans 12 bold", state="readonly")
        self.entryProducto.place(x=340, y=7, width=180)

        self.cargar_productos()

        lblPrecio = tk.Label(lblFrameInfFactura, text="Precio: ", bg="#d5d5d5", font="sans 12 bold")
        lblPrecio.place(x=525, y=10)
        self.entryPrecio = ttk.Entry(lblFrameInfFactura, font="sans 12 bold", state="readonly", justify="right")
        self.entryPrecio.place(x=590, y=7, width=180)

        self.entryProducto.bind("<<ComboboxSelected>>", self.actualizar_precio)

        lblCantidad = tk.Label(lblFrameInfFactura, text="Cantidad: ", bg="#d5d5d5", font="sans 12 bold")
        lblCantidad.place(x=775, y=10)
        self.entryCantidad = ttk.Entry(lblFrameInfFactura, font="sans 12 bold", justify="right")
        self.entryCantidad.place(x=860, y=7, width=180)

        treFrame = tk.Frame(frame_container, bg="#dddddd")
        treFrame.place(x=135, y=120, width=830, height=200)

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

        btnAgregar = tk.Button(lblFrameOpciones, text="Agregar", bg="#0288D1", font="sans 12 bold", command=self.registrar)
        btnAgregar.place(x=50, y=10, width=240, height=50)

        btnPagar = tk.Button(lblFrameOpciones, text="Pagar", bg="#0288D1", font="sans 12 bold", command=self.abrir_ventana_pago)
        btnPagar.place(x=400, y=10, width=240, height=50)

        btnVer = tk.Button(lblFrameOpciones, text="Ver", bg="#0288D1", font="sans 12 bold", command=self.abrir_ventana_factura)
        btnVer.place(x=750, y=10, width=240, height=50)

        self.label_suma_total = tk.Label(frame_container, text="Total a pagar: $ 0", bg="#d5d5d5", font="sans 25 bold")
        self.label_suma_total.place(x=360, y=335)

    def cargar_productos(self):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT nombre FROM inventario")
            productos = c.fetchall()
            self.entryProducto["values"] = [producto[0] for producto in productos]
            if not productos:
                print("No se encontraron productos.")
            conn.close()
        except sqlite3.Error as e:
            print(f"Error {e}: Carga de datos")

    def actualizar_precio(self, event):
        nombre_producto = self.entryProducto.get()
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT precio FROM inventario WHERE nombre = ?", (nombre_producto,))
            precio = c.fetchall()
            if (precio):
                self.entryPrecio.config(state="normal")
                self.entryPrecio.delete(0, tk.END)
                self.entryPrecio.insert(0, precio[0])
                self.entryPrecio.config(state="readonly")
            else:
                self.entryPrecio.config(state="normal")
                self.entryPrecio.delete(0, tk.END)
                self.entryPrecio.insert(0, "Precio no disponible")
                self.entryPrecio.config(state="readonly")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener el precio: {e}")
        finally:
            conn.close()

    def actualizar_total(self):
        total = 0.0
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values") [3])
            total += subtotal
        self.label_suma_total.config(text=f"Total a pagar: ${total:.2f}")

    def registrar(self):
        producto = self.entryProducto.get()
        precio = self.entryPrecio.get()
        cantidad = self.entryCantidad.get()

        if producto and precio and cantidad:
            try:
                cantidad = int(cantidad)
                if not self.verificar_stock(producto, cantidad):
                    messagebox.showerror("Error", "Stock insuficiente para el producto seleccionado,")
                    return
                precio = float(precio)
                subtotal = cantidad * precio

                self.tree.insert("", "end", values=(producto, f"{precio:.2f}", cantidad, f"{subtotal:.2f}"))

                self.entryProducto.set("")
                self.entryPrecio.config(state="normal")
                self.entryPrecio.delete(0, tk.END)
                self.entryPrecio.config(state="readonly")
                self.entryCantidad.delete(0, tk.END)

                self.actualizar_total()
            except ValueError:
                messagebox.showerror("Error", "Cantidad o precio no validos.")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos.")

    def verificar_stock(self, nombre_producto, cantidad):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT stock FROM inventario WHERE nombre = ?", (nombre_producto,))
            stock = c.fetchone()
            if stock and stock[0] >= cantidad:
                return True
            return False
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al verificar el stock: {e}")
            return False
        finally:
            conn.close()

    def obtener_total(self):
        total = 0.0
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values") [3])
            total += subtotal
        return total
    
    def abrir_ventana_pago(self):
        if not self.tree.get_children():
            messagebox.showerror("Error", "No hay articulos para pagar.")
            return
        
        ventana_pago = Toplevel(self)
        ventana_pago.title("Realizar Pago")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 400
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        ventana_pago.geometry(f"{window_width}x{window_height}+{x}+{y}")
        #ventana_pago.geometry("400x400")
        ventana_pago.config(bg="#d5d5d5")
        ventana_pago.resizable(False, False)

        ventana_pago.transient(self.master)  
        ventana_pago.grab_set()  
        ventana_pago.focus_set()  
        ventana_pago.lift()

        label_total = tk.Label(ventana_pago, bg="#d5d5d5", text=f"Total a pagar: ${self.obtener_total():.2f}", font= "sans 18 bold")
        label_total.place(x=70, y=20)

        label_cantidad_pagada = tk.Label(ventana_pago, bg="#d5d5d5", text="Cantidad pagada:", font="sans 14 bold")
        label_cantidad_pagada.place(x=100, y=90)
        entry_cantidad_pagada = ttk.Entry(ventana_pago, font="sans 14 bold")
        entry_cantidad_pagada.place(x=100, y=130)

        label_cambio = tk.Label(ventana_pago, bg="#d5d5d5", text="", font="sans 14 bold")
        label_cambio.place(x=100, y=190)

        def calcular_cambio():
            try:
                cantidad_pagada = float(entry_cantidad_pagada.get())
                total = self.obtener_total()
                cambio = cantidad_pagada - total
                if cambio < 0:
                    messagebox.showerror("Error", "La cantidad pagada es insuficiente.")
                    return
                label_cambio.config(text=f"Vuelto: ${cambio:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Cantidad pagada no válida.")

        boton_calcular = tk.Button(ventana_pago, text="Calcular vuelto", bg="#0288D1", font="sans 12 bold", command=calcular_cambio)
        boton_calcular.place(x=100, y=240, width=240, height=40)

        boton_pagar = tk.Button(ventana_pago, text="Pagar", bg="#0288D1", font="sans 12 bold", command=lambda: self.pagar(ventana_pago, entry_cantidad_pagada))
        boton_pagar.place(x=100, y=300, width=240, height=40)
    
    def pagar(self, ventana_pago, entry_cantidad_pagada):
        try:
            cantidad_pagada = float(entry_cantidad_pagada.get())
            total = self.obtener_total()
            cambio = cantidad_pagada - total
            if cambio < 0:
                messagebox.showerror("Error", "La cantidad pagada es insuficiente.")
                return
        
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            try:
                for child in self.tree.get_children():
                    item = self.tree.item(child, "values")
                    nombre_producto = item[0]
                    cantidad_vendida = int(item[2])
                    if not self.verificar_stock(nombre_producto, cantidad_vendida):
                        messagebox.showerror("Error", f"Stock insuficiente para el producto: {nombre_producto}")
                        return
                    
                    c.execute("INSERT INTO ventas (fac_numero, nombre_articulo, valor_articulo, cantidad, subtotal) VALUES (?,?,?,?,?)", (self.numero_factura_actual, nombre_producto, float(item[1]), cantidad_vendida, float(item[3])))

                    c.execute("UPDATE inventario SET stock = stock - ? WHERE nombre = ?", (cantidad_vendida, nombre_producto))

                conn.commit()
                messagebox.showinfo("Exito", "Venta registrada exitosamente")

                self.numero_factura_actual += 1
                self.mostrar_numero_factura()

                for child in self.tree.get_children():
                    self.tree.delete(child)
                self.label_suma_total.config(text="Total a pagar: $0")
                ventana_pago.destroy()
            
            except sqlite3.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"Error al registrar la venta: {e}")
            finally:
                conn.close()

        except ValueError:
            messagebox.showerror("Error", "Cantidad pagada no valida")

    def obtener_numero_factura_actual(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        try:
            c.execute("SELECT MAX(fac_numero) FROM ventas")
            max_factura = c.fetchone()[0]
            if max_factura:
                return max_factura + 1
            else:
                return 1
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener el numero de factura: {e}")
            return 1
        finally:
            conn.close()

    def mostrar_numero_factura(self):
        self.nroFactura.set(self.numero_factura_actual)

    def abrir_ventana_factura(self):
        ventana_factura = Toplevel(self)
        ventana_factura.title("Factura")        
        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        ventana_factura.geometry(f"{window_width}x{window_height}+{x}+{y}")
        #ventana_factura.geometry("800x500")
        ventana_factura.config(bg="#d5d5d5")
        ventana_factura.resizable(False, False)

        facturas = Label(ventana_factura, bg="#d5d5d5", text="Facturas registradas", font="sans 36 bold")
        facturas.place(x=150, y=15)

        treFrame = tk.Frame(ventana_factura, bg="#d5d5d5")
        treFrame.place(x=10, y=100, width=780, height=380)

        scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        tree_facturas = ttk.Treeview(treFrame, columns=("ID", "Factura", "Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command=tree_facturas.yview)
        scrol_x.config(command=tree_facturas.xview)

        tree_facturas.heading("#1", text="ID")
        tree_facturas.heading("#2", text="Factura")
        tree_facturas.heading("#3", text="Producto")
        tree_facturas.heading("#4", text="Precio")
        tree_facturas.heading("#5", text="Cantidad")
        tree_facturas.heading("#6", text="Subtotal")

        tree_facturas.column("ID", anchor="center")
        tree_facturas.column("Factura", anchor="center")
        tree_facturas.column("Producto", anchor="center")
        tree_facturas.column("Precio", anchor="center")
        tree_facturas.column("Cantidad", anchor="center")
        tree_facturas.column("Subtotal", anchor="center")

        tree_facturas.pack(expand=True, fill=BOTH)

        self.cargar_facturas(tree_facturas)

    def cargar_facturas(self, tree):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT * FROM ventas")
            facturas = c.fetchall()
            for factura in facturas:
                tree.insert("", "end", values=factura)
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al cargar las facturas: {e}")