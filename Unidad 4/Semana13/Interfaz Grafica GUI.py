import tkinter as tk

# Funcion para agregar datos a la lista
def agregar_dato():
    dato = campo_texto.get()
    if dato != "":
        lista_datos.insert(tk.END, dato)
        campo_texto.delete(0, tk.END)

# Función para limpiar el campo de texto y la lista
def limpiar_dato():
    campo_texto.delete(0, tk.END)
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
app = tk.Tk()
app.title("Aplicación de Lista de Datos")
app.geometry("600x600")
app.configure(bg="lightpink")


# Etiqueta de titulo
etiqueta_titulo = tk.Label(app, text="Ingresa un dato para agregar a la lista:",font=("currie", 12, "bold"))
etiqueta_titulo.pack(pady=10)  # Empacar con espacio alrededor

# (Entry)
campo_texto = tk.Entry(app, width=50, font=("currie", 15, "bold"))
campo_texto.pack(pady=10)

# Boton
boton_agregar = tk.Button(app, text="Agregar", command=agregar_dato, font=("currie", 15, "bold"))
boton_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(app, width=50, height=10, font=("currie", 15, "bold"))
lista_datos.pack(pady=10)

# Boton para limpiar el campo de texto y la lista
boton_limpiar = tk.Button(app, text="Limpiar", command=limpiar_dato, font=("currie", 15, "bold"))
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la aplicación
app.mainloop()

