import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x510")
ventana.config(bg="#1c1c1c")

# Pantalla pequeña (historial)
historial = tk.Label(
    ventana,
    text="",
    anchor="se",
    bg="#1c1c1c",
    fg="#a5a5a5",
    font=("Arial", 18)
)
historial.grid(row=0, column=0, columnspan=4, sticky="we", padx=10, pady=(25, 5))

# Pantalla principal
pantalla = tk.Entry(
    ventana,
    font=("Arial", 28),
    bd=0,
    justify="right",
    bg="#1c1c1c",
    fg="white",
    insertbackground="white"
)
pantalla.grid(row=1, column=0, columnspan=4, padx=10, pady=(0,15), ipady=15, sticky="we")

# Funciones
def click(valor):
    pantalla.insert(tk.END, valor)

def limpiar():
    pantalla.delete(0, tk.END)
    historial.config(text="")

def borrar():
    texto = pantalla.get()
    if texto:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, texto[:-1])

def igual():
    try:
        expresion = pantalla.get()
        resultado = eval(expresion)

        historial.config(text=expresion + " =")
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Botones
def boton(texto, fila, columna, bg, fg="white", comando=None):
    tk.Button(
        ventana,
        text=texto,
        font=("Arial", 14),
        bg=bg,
        fg=fg,
        bd=0,
        width=5,
        height=2,
        command=comando
    ).grid(row=fila, column=columna, padx=6, pady=6, sticky="nsew")

# Expandir columnas
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Colores
gris = "#333333"
gris_claro = "#505050"
naranja = "#ff9500"

# Fila 1
boton("AC",2,0,gris_claro, comando=limpiar)
boton("+/-",2,1,gris_claro)
boton("%",2,2,gris_claro)
boton("/",2,3,naranja, comando=lambda: click("/"))

# Fila 2
boton("7",3,0,gris, comando=lambda: click("7"))
boton("8",3,1,gris, comando=lambda: click("8"))
boton("9",3,2,gris, comando=lambda: click("9"))
boton("*",3,3,naranja, comando=lambda: click("*"))

# Fila 3
boton("4",4,0,gris, comando=lambda: click("4"))
boton("5",4,1,gris, comando=lambda: click("5"))
boton("6",4,2,gris, comando=lambda: click("6"))
boton("-",4,3,naranja, comando=lambda: click("-"))

# Fila 4
boton("1",5,0,gris, comando=lambda: click("1"))
boton("2",5,1,gris, comando=lambda: click("2"))
boton("3",5,2,gris, comando=lambda: click("3"))
boton("+",5,3,naranja, comando=lambda: click("+"))

# Fila 5
boton("0",6,0,gris, comando=lambda: click("0"))
boton(".",6,1,gris, comando=lambda: click("."))
boton("⌫",6,2,gris_claro, comando=borrar)
boton("=",6,3,naranja, comando=igual)

ventana.mainloop()