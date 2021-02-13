from tkinter import *

import LEDino

# Crea la ventana de la aplicación
root = Tk()
root.title("LEDino")
root.minsize(400,310)
root.maxsize(700,400)


# Interfaz para cambiar color

# Titulo
tituloColor = Label(root, text = "Color", font= 'Default 24')
tituloColor.grid(row = 0, column = 0, pady = 5, padx = 5, sticky=W)

# Botones para colores comunes
bRojo = Button(root, 
    text="rojo", 
    width = 4,
    command = lambda: LEDino.color("rojo"))
bRojo.grid(row = 1, column = 0)

bVerde = Button(root,
    text="verde", 
    width = 4,
    command = lambda: LEDino.color("verde"))
bVerde.grid(row = 1, column = 1)

bAzul = Button(root, 
    text="azul", 
    width = 4,
    command = lambda: LEDino.color("azul"))
bAzul.grid(row = 1, column = 2)

bBlanco = Button(root, 
    text="blanco", 
    width = 4,
    command = lambda: LEDino.color("blanco"))
bBlanco.grid(row = 1, column = 3)

bApagado = Button(root, 
    text="apagar", 
    width = 4,
    command = lambda: LEDino.color("apagado"))
bApagado.grid(row = 1, column = 4)


# Colores custom

# Muestra de color
muestra = Canvas(root, bg = '#000', height = 20, width=50, highlightbackground='grey')
muestra.grid(row=5,column=1, pady=5, padx=5, sticky=W)
def actualizarMuestra(rojo, verde, azul):
    muestra.config(bg=LEDino.colores2hexa(rojo,verde,azul))

# Canal Rojo
lCanalRojo = Label(root, text = "Rojo", font='Default 16')
lCanalRojo.grid(row=2,column=0,padx=10,sticky=E)
escalaRojo = Scale(root, from_=0, to=255, orient=HORIZONTAL,
    command=lambda _ : actualizarMuestra(escalaRojo.get(),escalaVerde.get(),escalaAzul.get()))
escalaRojo.grid(row=2, column=1, columnspan = 4, sticky=EW, padx = 10)

# Canal Verde
lCanalVerde = Label(root, text = "Verde", font='Default 16')
lCanalVerde.grid(row=3,column=0,padx=10, sticky=E)
escalaVerde = Scale(root, from_=0, to=255, orient=HORIZONTAL,
    command=lambda _ : actualizarMuestra(escalaRojo.get(),escalaVerde.get(),escalaAzul.get()))
escalaVerde.grid(row=3, column=1, columnspan = 4, sticky=EW, padx = 10)

# Canal Azul
lCanalAzul = Label(root, text = "Azul", font='Default 16')
lCanalAzul.grid(row=4,column=0,padx=10, sticky=E)
escalaAzul = Scale(root, from_=0, to=255, orient=HORIZONTAL,
    command=lambda _ : actualizarMuestra(escalaRojo.get(),escalaVerde.get(),escalaAzul.get()))
escalaAzul.grid(row=4, column=1, columnspan = 4, sticky=EW, padx = 10)

# Color para enviar
bEnviar = Button(root,
    text="Enviar",
    width=4,
    # Crea el mensaje en el momento
    command= lambda:LEDino.color(LEDino.crearColorCustom(escalaRojo.get(), escalaVerde.get(), escalaAzul.get()))
    )
bEnviar.grid(row=5,column=0, sticky=E, pady = 10)


# Separador

separador = Frame(root, bg = 'grey')
separador.grid(row = 6, column = 0, columnspan = 5, sticky=EW, padx=10, ipady = 1)


# Interfaz para parpadear

# Titulo
tituloParpadeo = Label(root, text = "Parpadeo", font= 'Default 24')
tituloParpadeo.grid(row = 7, column = 0, columnspan=2, pady = 5, padx = 5, sticky=W)

bParpadear = Button(root,
    text="parpadear",
    width=4,
    command=lambda: LEDino.parpadear("ence"))
bParpadear.grid(row = 8, column = 0, pady = 10) 

bNoParpadear = Button(root,
    text="no parp...",
    width=4,
    command=lambda: LEDino.parpadear("apag"))
bNoParpadear.grid(row = 8, column = 1, pady = 10) 

bAlternar = Button(root,
    text="alternar",
    width=4,
    command=lambda: LEDino.parpadear("camb"))
bAlternar.grid(row = 8, column = 2, pady = 10)


# Configuración de las celdas:
numColumns, numRows = root.grid_size()
for column in range(numColumns):
    root.grid_columnconfigure(column, weight = 1 )
for row in range(numRows):
    root.grid_rowconfigure(row, weight = 1)

# Inicia el loop infinito
root.mainloop()