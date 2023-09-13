import tkinter as tk
from tkinter import ttk

def analizar_cadena():
    entrada = entrada_texto.get("1.0", "end-1c")
    elementos = []
    estado = 0
    indice = 0
    cadena = entrada + '$'

    while (indice <= (len(cadena) - 1) and estado == 0):
        lexema = ''
        token = 'error'
        numero = -1

        while (indice <= (len(cadena) - 1) and estado != 20):
            if estado == 0:
                if (cadena[indice].isspace()):
                    estado = 0
                elif cadena[indice].isalpha() or cadena[indice] == '_':
                    estado = 4
                    lexema += cadena[indice]
                    token = 'id'
                    numero = 1
                elif cadena[indice].isnumeric():
                    estado = 4
                    lexema += cadena[indice]
                    indice += 1
                    while indice < len(cadena) and cadena[indice].isnumeric():
                        lexema += cadena[indice]
                        indice += 1
                    token = 'constante'
                    numero = 13
                    estado = 20
                elif cadena[indice] == '=':
                    lexema += cadena[indice]
                    token = 'asignación'
                    estado = 5
                    numero = 8
                elif cadena[indice] == '>':
                    lexema += cadena[indice]
                    token = 'opRelacional'
                    estado = 5
                    numero = 17
                elif cadena[indice] == '<':
                    lexema += cadena[indice]
                    token = 'opRelacional'
                    estado = 5
                    numero = 17
                elif cadena[indice] == '!':
                    lexema += cadena[indice]
                    estado = 5
                    numero = 17
                elif cadena[indice] == ';':
                    lexema += cadena[indice]
                    token = ';'
                    estado = 20
                    numero = 2
                elif cadena[indice] == '+':
                    lexema += cadena[indice]
                    token = 'opSuma'
                    estado = 20
                    numero = 14
                elif cadena[indice] == '-':
                    lexema += cadena[indice]
                    token = 'opSuma'
                    estado = 20
                    numero = 14
                elif cadena[indice] == '*':
                    lexema += cadena[indice]
                    token = 'opMultiplicacion'
                    estado = 20
                    numero = 16
                elif cadena[indice] == '/':
                    lexema += cadena[indice]
                    token = 'opMultiplicacion'
                    estado = 20
                    numero = 16
                elif cadena[indice] == ',':
                    lexema += cadena[indice]
                    token = ','
                    estado = 20
                    numero = 3
                elif cadena[indice] == '(':
                    lexema += cadena[indice]
                    token = '('
                    estado = 20
                    numero = 4
                elif cadena[indice] == ')':
                    lexema += cadena[indice]
                    token = ')'
                    estado = 20
                    numero = 5
                elif cadena[indice] == '{':
                    lexema += cadena[indice]
                    token = '{'
                    estado = 20
                    numero = 6
                elif cadena[indice] == '}':
                    lexema += cadena[indice]
                    token = '}'
                    estado = 20
                    numero = 7
                elif cadena[indice] == '|':
                    lexema += cadena[indice]
                    estado = 15
                    numero = 17
                elif cadena[indice] == '$':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'Pesos'
                    numero = 18
                elif cadena[indice] == '&':
                    lexema += cadena[indice]
                    estado = 16
                    numero = 17
                else:
                    estado = 20
                    token = 'error'
                    lexema = cadena[indice]
                indice += 1

            elif estado == 4:
                if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice] == '_':
                    estado = 4
                    lexema += cadena[indice]
                    token = 'id'
                    numero = 1
                    indice += 1
                else:
                    estado = 20

            elif estado == 5:
                if cadena[indice] == '=':
                    lexema += cadena[indice]
                    token = 'opRelacional'
                    numero = 17
                    estado = 20
                    indice += 1
                else:
                    estado = 20

            elif estado == 15:
                if cadena[indice] == '|':
                    lexema += cadena[indice]
                    token = 'opLogico'
                    numero = 15
                    estado = 20
                    indice += 1
                else:
                    estado = 20

            elif estado == 16:
                if cadena[indice] == '&':
                    lexema += cadena[indice]
                    token = 'opLogico'
                    numero = 15
                    estado = 20
                    indice += 1
                else:
                    estado = 20
            

        estado = 0
        elementos.append({'token': token, 'lexema': lexema, 'numero': numero})

    for elemento in elementos:
        for elemento in elementos:
            if elemento['lexema'] == "if":
                elemento['token'] = "condicional SI"
                elemento['numero'] = 9
            elif elemento['lexema'] == "while":
                elemento['token'] = "while"
                elemento['numero'] = 10
            elif elemento['lexema'] == "return":
                elemento['token'] = "return"
                elemento['numero'] = 11
            elif elemento['lexema'] == "else":
                elemento['token'] = "else"
                elemento['numero'] = 12
            elif elemento['lexema'] == "int":
                elemento['token'] = "tipo de dato"
                elemento['numero'] = 19
            elif elemento['lexema'] == "float":
                elemento['token'] = "tipo de dato"
                elemento['numero'] = 19
            elif elemento['lexema'] == "char":
                elemento['token'] = "tipo de dato"
                elemento['numero'] = 19
            elif elemento['lexema'] == "void":
                elemento['token'] = "Tipo de dato"
                elemento['numero'] = 19
            

    print(elemento)

    for row in tabla.get_children():
        tabla.delete(row)

    for elemento in elementos:
        tabla.insert("", "end", values=(elemento['lexema'], elemento['token'], elemento['numero']))

ventana = tk.Tk()
ventana.title("Analizador Léxico")

etiqueta = tk.Label(ventana, text="Ingrese la cadena:")
etiqueta.pack()

entrada_texto = tk.Text(ventana, height=10, width=30)
entrada_texto.pack()

boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_cadena)
boton_analizar.pack()

cuadro_derecho = tk.Frame(ventana, width=30)
cuadro_derecho.pack(side=tk.LEFT, padx=10)

tabla = ttk.Treeview(ventana, columns=("Lexema", "Token", "Número"), show="headings")
tabla.heading("Lexema", text="Lexema")
tabla.heading("Token", text="Token")
tabla.heading("Número", text="Número")
tabla.pack(pady=10)

ventana.mainloop()
