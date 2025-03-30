import tkinter as tk
from tkinter import messagebox

class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista de tareas
        self.tareas = []

        # Campo de entrada para nueva tarea
        self.entry_tarea = tk.Entry(self.root, width=60)
        self.entry_tarea.grid(row=0, column=0, padx=10, pady=10)

        # BotOn para agregar tarea
        self.boton_agregar = tk.Button(self.root, text="Añadir Tarea", width=20, command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=1, padx=10, pady=10)

        # Lista de tareas (Listbox)
        self.listbox_tareas = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40, height=10)
        self.listbox_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # BotOn para marcar como completada
        self.boton_completar = tk.Button(self.root, text="Marcar como Completada", width=20, command=self.marcar_completada)
        self.boton_completar.grid(row=2, column=0, padx=10, pady=10)

        # BotOn para eliminar tarea
        self.boton_eliminar = tk.Button(self.root, text="Eliminar Tarea", width=20, command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

        # Vincular la tecla Enter con agregar tarea
        self.root.bind("<Return>", self.agregar_tarea_por_tecla)

    def agregar_tarea(self, event=None):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.tareas.append(tarea)
            self.actualizar_lista()
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def agregar_tarea_por_tecla(self, event):
        self.agregar_tarea()

    def actualizar_lista(self):
        """Actualiza el Listbox con las tareas actuales."""
        self.listbox_tareas.delete(0, tk.END)  # Limpiar el Listbox
        for tarea in self.tareas:
            self.listbox_tareas.insert(tk.END, tarea)

    def marcar_completada(self):
        """Marca la tarea seleccionada como completada."""
        try:
            seleccionada = self.listbox_tareas.curselection()
            if seleccionada:
                index = seleccionada[0]
                tarea = self.tareas[index]
                tarea_completada = f"{tarea} - Completada"
                self.tareas[index] = tarea_completada
                self.actualizar_lista()
            else:
                messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada."""
        try:
            seleccionada = self.listbox_tareas.curselection()
            if seleccionada:
                index = seleccionada[0]
                self.tareas.pop(index)
                self.actualizar_lista()
            else:
                messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")


# Crear la ventana principal y la aplicación
root = tk.Tk()
app = ListaDeTareasApp(root)

# Ejecutar la aplicación
root.mainloop()
