import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import json
from os.path import exists

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Agenda Personal")
root.geometry("620x700")
root.configure(bg="lightpink")

# Nombre del archivo JSON para guardar los eventos
archivo_agenda = "agenda.json"

# Función para guardar los eventos en un archivo JSON
def guardar_eventos():
    eventos = []
    for item in tree.get_children():
        eventos.append(tree.item(item)["values"])
    with open(archivo_agenda, "w") as archivo:
        json.dump(eventos, archivo)
    print("Eventos guardados en agenda.json")

# Función para cargar los eventos desde un archivo JSON
def cargar_eventos():
    if exists(archivo_agenda):
        with open(archivo_agenda, "r") as archivo:
            eventos = json.load(archivo)
            for evento in eventos:
                tree.insert("", "end", values=evento)
        print("Eventos cargados desde agenda.json")

# Frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

# Frame para la entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.grid(row=1, column=0, padx=6, pady=6)

# Frame para los botones
frame_botones = tk.Frame(root)
frame_botones.grid(row=2, column=0, padx=5, pady=5)

# Treeview para mostrar los eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.grid(row=0, column=0, sticky="nsew")

# Etiquetas y entradas
tk.Label(frame_entrada, text="Fecha").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Label(frame_entrada, text="Hora").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Label(frame_entrada, text="Descripción").grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Calendario para seleccionar la fecha
fecha = Calendar(frame_entrada, selectmode="day")
fecha.grid(row=0, column=1, padx=6, pady=6)

# Entrada para la descripción
descripcion = tk.Entry(frame_entrada)
descripcion.grid(row=2, column=1, padx=3, pady=3)

# Menú desplegable para la hora
hora_opciones = [
    "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
    "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"
]
hora_seleccionada = tk.StringVar()
hora_seleccionada.set(hora_opciones[0])  # Valor predeterminado

hora_menu = tk.OptionMenu(frame_entrada, hora_seleccionada, *hora_opciones)
hora_menu.grid(row=1, column=1, padx=10, pady=10)

# Funciones para agregar, eliminar y salir
def agregar_evento():
    fecha_seleccionada = fecha.get_date()
    hora_evento = hora_seleccionada.get()  # Obtener la hora seleccionada
    descripcion_evento = descripcion.get()
    if fecha_seleccionada and hora_evento and descripcion_evento:
        tree.insert("", "end", values=(fecha_seleccionada, hora_evento, descripcion_evento))
        hora_seleccionada.set(hora_opciones[0])  # Resetear la hora a la opción predeterminada
        descripcion.delete(0, tk.END)
        guardar_eventos()  # Guardar automáticamente después de agregar un evento
    else:
        messagebox.showerror("Error", "Por favor complete todos los datos")

def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmación", "¿Estás segura de eliminar este evento?"):
            tree.delete(seleccionado)
            guardar_eventos()  # Guardar automáticamente después de eliminar un evento
    else:
        messagebox.showwarning("Advertencia", "Por favor selecciona un evento para eliminar.")

def salir():
    guardar_eventos()  # Guardar los eventos cuando se cierre la aplicación
    root.quit()

# Crear los botones
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento, bg="lightblue", fg="black")
btn_agregar.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="lightblue", fg="black")
btn_eliminar.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

btn_salir = tk.Button(frame_botones, text="Salir", command=salir, bg="lightblue", fg="black")
btn_salir.grid(row=3, column=0, padx=5, pady=5, sticky="ew")


# Cargar los eventos desde el archivo JSON al iniciar
cargar_eventos()

# Iniciar la aplicación
root.mainloop()
