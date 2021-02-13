from tkinter import *
import LEDino

# Crea la ventana de la aplicación
root = Tk()
root.title("LEDino")
root.minsize(400,400)
root.maxsize(700,500)
for column in range(5):
    root.grid_columnconfigure(column, weight = 1 )


# Interfaz para cambiar color

# Titulo
tiuloColor = Label(root, text = "Color", font= 'Default 24')
tiuloColor.grid(row = 0, column = 0, pady = 5, padx = 5)

# Botones para colores comunes
btnRojo = Button(root, 
    text="rojo", 
    width = 4,
    command = lambda: LEDino.color("rojo"))
btnRojo.grid(row = 1, column = 0)

btnVerde = Button(root,
    text="verde", 
    width = 4,
    command = lambda: LEDino.color("verde"))
btnVerde.grid(row = 1, column = 1)

btnAzul = Button(root, 
    text="azul", 
    width = 4,
    command = lambda: LEDino.color("azul"))
btnAzul.grid(row = 1, column = 2)

btnBlanco = Button(root, 
    text="blanco", 
    width = 4,
    command = lambda: LEDino.color("blanco"))
btnBlanco.grid(row = 1, column = 3)

btnApagado = Button(root, 
    text="apagar", 
    width = 4,
    command = lambda: LEDino.color("apagado"))
btnApagado.grid(row = 1, column = 4)


# Colores custom

# Muestra de color
muestra = Canvas(root, bg = '#000', height = 20, width=50, highlightbackground='grey')
muestra.grid(row=5,column=1, pady=5, padx=5, sticky=W)
def actualizarMuestra(rojo, verde, azul):
    muestra.config(bg=LEDino.colores2hexa(rojo,verde,azul))

# Canal Rojo
lCanalRojo = Label(root, text = "Rojo", font='Default 16')
lCanalRojo.grid(row=2,column=0,padx=5)
escalaRojo = Scale(root, from_=0, to=255, orient=HORIZONTAL,
    command=lambda _ : actualizarMuestra(escalaRojo.get(),escalaVerde.get(),escalaAzul.get()))
escalaRojo.grid(row=2, column=1, columnspan = 4, sticky=EW, padx = 20)

# Canal Verde
lCanalVerde = Label(root, text = "Verde", font='Default 16')
lCanalVerde.grid(row=3,column=0,padx=5)
escalaVerde = Scale(root, from_=0, to=255, orient=HORIZONTAL,
    command=lambda _ : actualizarMuestra(escalaRojo.get(),escalaVerde.get(),escalaAzul.get()))
escalaVerde.grid(row=3, column=1, columnspan = 4, sticky=EW, padx = 20)

# Canal Azul
lCanalAzul = Label(root, text = "Azul", font='Default 16')
lCanalAzul.grid(row=4,column=0,padx=5)
escalaAzul = Scale(root, from_=0, to=255, orient=HORIZONTAL,
    command=lambda _ : actualizarMuestra(escalaRojo.get(),escalaVerde.get(),escalaAzul.get()))
escalaAzul.grid(row=4, column=1, columnspan = 4, sticky=EW, padx = 20)

# Color para enviar
bEnviar = Button(root,
    text="Enviar",
    width=4,
    # Crea el mensaje en el momento
    command= lambda:LEDino.color(LEDino.crearColorCustom(escalaRojo.get(), escalaVerde.get(), escalaAzul.get()))
    )
bEnviar.grid(row=5,column=0, sticky=E)




# Inicia el loop infinito
root.mainloop()