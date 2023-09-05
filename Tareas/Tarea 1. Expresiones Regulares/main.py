import re
import tkinter as tk

def validar_correo():
    text = correo_entrada.get()
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    mostrar_resultado(validar(text, pattern), 0)

def validar_fecha():
    text = fecha_entrada.get()
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    mostrar_resultado(validar(text, pattern), 1)

def validar_hora():
    text = hora_entrada.get()
    pattern = r"^([01]\d|2[0-3]):([0-5]\d)$"
    mostrar_resultado(validar(text, pattern), 2)

def validar_ip():
    text = ip_entrada.get()
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    mostrar_resultado(validar(text, pattern), 3)

def validar(text, pattern):
    return re.match(pattern, text)

def mostrar_resultado(is_valid, row):
    if is_valid:
        resultados[row].config(text="Entrada válida", fg="green")
    else:
        resultados[row].config(text="Entrada inválida", fg="red")

app = tk.Tk()
app.title("Validador de expresiones")

resultados = []

# Correo electrónico
correo_label = tk.Label(app, text="Correo electrónico:")
correo_label.grid(row=0, column=0, padx=20, pady=5, sticky=tk.W)
correo_entrada = tk.Entry(app, width=30)
correo_entrada.grid(row=0, column=1, padx=20, pady=5)
correo_boton = tk.Button(app, text="Validar", command=validar_correo)
correo_boton.grid(row=0, column=2, padx=20, pady=5)
resultados.append(tk.Label(app, text=""))
resultados[-1].grid(row=0, column=3, padx=20, pady=5)

# Fecha
fecha_label = tk.Label(app, text="Fecha (DD/MM/YYYY):")
fecha_label.grid(row=1, column=0, padx=20, pady=5, sticky=tk.W)
fecha_entrada = tk.Entry(app, width=30)
fecha_entrada.grid(row=1, column=1, padx=20, pady=5)
fecha_boton = tk.Button(app, text="Validar", command=validar_fecha)
fecha_boton.grid(row=1, column=2, padx=20, pady=5)
resultados.append(tk.Label(app, text=""))
resultados[-1].grid(row=1, column=3, padx=20, pady=5)

# Hora
hora_label = tk.Label(app, text="Hora (HH:MM):")
hora_label.grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)
hora_entrada = tk.Entry(app, width=30)
hora_entrada.grid(row=2, column=1, padx=20, pady=5)
hora_boton = tk.Button(app, text="Validar", command=validar_hora)
hora_boton.grid(row=2, column=2, padx=20, pady=5)
resultados.append(tk.Label(app, text=""))
resultados[-1].grid(row=2, column=3, padx=20, pady=5)

# Dirección IP
ip_label = tk.Label(app, text="Dirección IP:")
ip_label.grid(row=3, column=0, padx=20, pady=5, sticky=tk.W)
ip_entrada = tk.Entry(app, width=30)
ip_entrada.grid(row=3, column=1, padx=20, pady=5)
ip_boton = tk.Button(app, text="Validar", command=validar_ip)
ip_boton.grid(row=3, column=2, padx=20, pady=5)
resultados.append(tk.Label(app, text=""))
resultados[-1].grid(row=3, column=3, padx=20, pady=5)

app.mainloop()
