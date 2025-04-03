import tkinter as tk
from tkinter import messagebox
import json
import os

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")  # Titulo de la ventana
root.geometry("620x480")
root.config(bg="#f0f0f0")

# Ruta para el archivo
tareas_archivo = 'tareas.json'

# Definimos la función para cargar las tareas
def cargar_tareas():
    if os.path.exists(tareas_archivo):  # Para ver si nuestro archivo existe
        with open(tareas_archivo, 'r') as archivo:
            try:
                tareas_cargadas = json.load(archivo)  # Cargar tareas
            except json.decoder.JSONDecodeError:  # Para ver si el archivo está vacío o presenta errores
                tareas_cargadas = []
    else:
        tareas_cargadas = []
    return tareas_cargadas

# Definimos la función para guardar tareas
def guardar_tareas():
    tareas_lista = lista_tareas.get(0, tk.END)  # Obtener las tareas desde el Listbox
    with open(tareas_archivo, 'w', encoding='utf-8') as archivo:  # Abrir archivo en modo escritura de texto
        json.dump(list(tareas_lista), archivo, ensure_ascii=False, indent=4)  # Guardar las tareas como lista en JSON

# Definimos la función para agregar tareas
def agregar_tarea():
    tarea = entry_tarea.get()  # Obtenemos el texto desde el campo de entrada (Entry)
    if tarea:  # Verificamos si la tarea no está vacía
        lista_tareas.insert(tk.END, tarea)  # Añadimos la tarea a la lista
        entry_tarea.delete(0, tk.END)  # Limpiamos el campo de entrada
        guardar_tareas()  # Guardamos las tareas al archivo
    else:
        messagebox.showwarning('Advertencia', 'La tarea no puede estar vacía')

# Función para marcar la tarea como completada
def marcar_completada():
    tarea_seleccionada = lista_tareas.curselection()  # Obtener la tarea seleccionada
    if tarea_seleccionada:  # Verificar si hay alguna tarea seleccionada
        tarea_index = tarea_seleccionada[0]
        tarea_texto = lista_tareas.get(tarea_index)  # Obtener el texto de la tarea
        lista_tareas.delete(tarea_index)  # Eliminar la tarea de la lista
        lista_tareas.insert(tarea_index, tarea_texto + " (Completada)")  # Volver a agregarla con el estado 'Completada'
        guardar_tareas()  # Guardar las tareas al archivo


# Función para eliminar la tarea seleccionada
def eliminar_tarea():
    tarea_seleccionada = lista_tareas.curselection()  # Obtener la tarea seleccionada
    if tarea_seleccionada:  # Verificar si hay alguna tarea seleccionada
        lista_tareas.delete(tarea_seleccionada)  # Eliminar la tarea de la lista
        guardar_tareas()  # Guardar las tareas al archivo


# Definimos función para cerrar la aplicación
def cerrar_aplicacion(event):
    root.quit()  # Salir de la aplicación cuando se presione la tecla Escape

# Campo de entrada para las tareas
entry_tarea = tk.Entry(root, width=40, font=("Arial", 14), bg="#ffffff", fg="#333333", borderwidth=2, relief="solid")
entry_tarea.pack(pady=10)

# Lista para mostrar las tareas
lista_tareas = tk.Listbox(root, width=50, height=10, font=("Arial", 12), selectmode=tk.SINGLE, bg="#fafafa", fg="#333333", selectbackground="#4CAF50", selectforeground="#ffffff")
lista_tareas.pack(pady=10)

# Cargar las tareas desde el archivo y mostrarlas en la lista
tareas = cargar_tareas()
for tarea in tareas:
    lista_tareas.insert(tk.END, tarea)

# Botones para agregar, marcar como completada y eliminar tareas
btn_agregar = tk.Button(root, text="Agregar Tarea", width=20, font=("Arial", 12), bg="#4CAF50", fg="#ffffff", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completada = tk.Button(root, text="Marcar como Completada", width=20, font=("Arial", 12), bg="#2196F3", fg="#ffffff", command=marcar_completada)
btn_completada.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", width=20, font=("Arial", 12), bg="#F44336", fg="#ffffff", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Configuración de atajos de teclado
root.bind("<Return>", lambda event: agregar_tarea())  # Tecla Enter para agregar tarea
root.bind("<c>", lambda event: marcar_completada())  # Tecla C para marcar tarea como completada
root.bind("<Delete>", lambda event: eliminar_tarea())  # Tecla Delete para eliminar tarea
root.bind("<d>", lambda event: eliminar_tarea())  # Tecla D para eliminar tarea
root.bind("<Escape>", cerrar_aplicacion)  # Tecla Escape para cerrar la aplicación


# Iniciar la interfaz grafica
root.mainloop()





