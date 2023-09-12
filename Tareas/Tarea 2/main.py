import tkinter as tk
from tkinter import ttk

def analizar_cadena():
    cadena0 = entrada_texto.get("1.0", "end-1c")
    elementos = []
    estado = 0
    indice = 0
    cadena = cadena0 + '$'
    
    # Diccionario de mapeo de lexemas a tokens y números
    mapeo = {
        "var1": {"token": "id", "numero": 1},
        ";": {"token": ";", "numero": 2},
        ",": {"token": ",", "numero": 3},
        "(": {"token": "(", "numero": 4},
        ")": {"token": ")", "numero": 5},
        "{": {"token": "{", "numero": 6},
        "}": {"token": "}", "numero": 7},
        "=": {"token": "asignación", "numero": 8},
        "if": {"token": "condicional SI", "numero": 9},
        "while": {"token": "while", "numero": 10},
        "return": {"token": "return", "numero": 11},
        "else": {"token": "else", "numero": 12},
        "1": {"token": "constante", "numero": 13},
        "+": {"token": "opSuma", "numero": 14},
        "-": {"token": "opSuma", "numero": 14},
        "||": {"token": "opLogico", "numero": 15},
        "&&": {"token": "opLogico", "numero": 15},
        "*": {"token": "opMultiplicacion", "numero": 16},
        "/": {"token": "opMultiplicacion", "numero": 16},
        "==": {"token": "opRelacional", "numero": 17},
        "<": {"token": "opRelacional", "numero": 17},
        "<=": {"token": "opRelacional", "numero": 17},
        ">": {"token": "opRelacional", "numero": 17},
        ">=": {"token": "opRelacional", "numero": 17},
        "!=": {"token": "opRelacional", "numero": 17},
        "$": {"token": "pesos", "numero": 18},
        "int": {"token": "tipo de dato", "numero": 19},
        "float": {"token": "tipo de dato", "numero": 19},
        "char": {"token": "tipo de dato", "numero": 19},
        "void": {"token": "tipo de dato", "numero": 19},
    }
    
    while (indice <= (len(cadena) - 1) and estado == 0):
        lexema = ''
        token = 'error'
        while (indice <= (len(cadena) - 1) and estado != 20):
            if estado == 0:
                if (cadena[indice].isspace()):
                    estado = 0
                elif cadena[indice].isalpha() or cadena[indice] == '_':
                    estado = 4
                    lexema += cadena[indice]
                    token = 'id'
                elif cadena[indice] == '$':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'pesos'
                elif cadena[indice] == '=':
                    lexema += cadena[indice]
                    token = 'asignación'
                    estado = 5
                elif cadena[indice] == '+' or cadena[indice] == '-':
                    lexema += cadena[indice]
                    token = 'opSuma'
                    estado = 5
                elif cadena[indice] == '|' or cadena[indice] == '&':
                    lexema += cadena[indice]
                    estado = 6
                elif cadena[indice] == '<' or cadena[indice] == '>' or cadena[indice] == '!':
                    lexema += cadena[indice]
                    token = 'opRelacional'
                    estado = 9
                elif cadena[indice] == '(':
                    lexema += cadena[indice]
                    token = '('
                    estado = 20
                elif cadena[indice] == ')':
                    lexema += cadena[indice]
                    token = ')'
                    estado = 20
                elif cadena[indice] == '{':
                    lexema += cadena[indice]
                    token = '{'
                    estado = 20
                elif cadena[indice] == '}':
                    lexema += cadena[indice]
                    token = '}'
                    estado = 20
                elif cadena[indice] == ',':
                    lexema += cadena[indice]
                    token = ','
                    estado = 20
                elif cadena[indice] == ';':
                    lexema += cadena[indice]
                    token = ';'
                    estado = 20
                elif cadena[indice] == '*':
                    lexema += cadena[indice]
                    token = 'opMultiplicacion '
                    estado = 20
                elif cadena[indice] == '/':
                    lexema += cadena[indice]
                    token = 'opMultiplicacion '
                    estado = 20
                elif cadena[indice] == '<':
                    lexema += cadena[indice]
                    token = '<'
                    estado = 20
                elif cadena[indice] == '>':
                    lexema += cadena[indice]
                    token = '>'
                    estado = 20
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
                    indice += 1
                else:
                    estado = 20
            elif estado == 5:
                if cadena[indice] != '=':
                    estado = 20
                else:
                    estado = 20
                    lexema += cadena[indice]
                    token = 'opRelacional'
                    indice += 1
            elif estado == 6:
                if cadena[indice] == '|':
                    lexema += cadena[indice]
                    estado = 7
                    token = 'opLogico'
                    indice += 1
                elif cadena[indice] == '&':
                    lexema += cadena[indice]
                    estado = 8
                    token = 'opLogico'
                    indice += 1
                else:
                    estado = 20
    
            elif estado == 7:
                if cadena[indice] == '|':
                    lexema += cadena[indice]
                    estado = 20
                    token = 'opLogico'
                    indice += 1
                else:
                    estado = 20
    
            elif estado == 8:
                if cadena[indice] == '&':
                    lexema += cadena[indice]
                    estado = 20
                    token = 'opLogico'
                    indice += 1
                else:
                    estado = 20
    
            elif estado == 9:
                if cadena[indice] == '=':
                    lexema += cadena[indice]
                    estado = 20
                    token = 'opRelacional'
                    indice += 1
                else:
                    estado = 20
    
        estado = 0
        # Buscar el número asociado al token en el diccionario de mapeo
        numero = mapeo.get(lexema, {"numero": -1})["numero"]
        elementos.append({'token': token, 'lexema': lexema, 'numero': numero})
    
    # Limpiar la tabla
    for row in tabla.get_children():
        tabla.delete(row)
    
    # Llenar la tabla con los resultados
    for elemento in elementos:
        tabla.insert("", "end", values=(elemento['lexema'], elemento['token'], elemento['numero']))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Léxico")

# Crear el cuadro de texto
etiqueta = tk.Label(ventana, text="Ingrese la cadena:")
etiqueta.pack()

entrada_texto = tk.Text(ventana, height=10, width=30)
entrada_texto.pack()

# Crear el botón
boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_cadena)
boton_analizar.pack()

# Crear el cuadro del lado derecho
cuadro_derecho = tk.Frame(ventana, width=30)
cuadro_derecho.pack(side=tk.LEFT, padx=10)

# Crear la tabla
tabla = ttk.Treeview(ventana, columns=("Lexema", "Token", "Número"), show="headings")
tabla.heading("Lexema", text="Lexema")
tabla.heading("Token", text="Token")
tabla.heading("Número", text="Número")
tabla.pack(pady=10)

ventana.mainloop()

#var1 ; , ( ) { } = if while return else 1 + - || && * /  == < <= > >= != int
