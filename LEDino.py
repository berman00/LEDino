'''
Programa para interactuar con un microconrolador
en una red local, para controlar un LED.

Valentin Berman 11/2/21
'''

import socket


# Funciones

def validarColor(color):
    
    colorLista = color.split(':')
    if len(colorLista) != 3:
        return False
    
    for item in colorLista:
        if not item.isdecimal():
            return False
        if int(item) < 0 or int(item) > 255:
            return False
    
    return True


def crearConfig():
    print("No exite un archivo de configuración.\nSe requiere la dirección ip y el puerto del arduino:")
    ipDoc = input("ip: ")
    puertoDoc = input("puerto: ")

    with open("/Users/valen/Codigo/LEDino/LEDino.cfg", 'w') as config:
        config.write(ipDoc + '\n' + puertoDoc)


def enviarMensaje(mensaje):

    try:
        with open("/Users/valen/Codigo/LEDino/LEDino.cfg", 'r') as config:
            ip = config.readline().replace('\n', '')
            puerto = int(config.readline())
    except FileNotFoundError:
        crearConfig()
        with open("/Users/valen/Codigo/LEDino/LEDino.cfg", 'r') as config:
            ip = config.readline().replace('\n', '')
            puerto = int(config.readline())
    
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as UDP_socket:
        UDP_socket.sendto(mensaje.encode(), (ip, puerto))

def crearColorCustom(rojo, verde, azul):
    '''
    Crea un string para enviar al arduino y que seleccione cualquier color
    '''

    return "%d:%d:%d" % (rojo, verde, azul)

def colores2hexa(rojo, verde, azul):
    '''
    Crea un string en el formato hexadecimal a partir de 3 enteros de colores
    '''

    hexRojo = hex(rojo).replace('0x','')
    if len(hexRojo) < 2: hexRojo = '0'+hexRojo    
    hexVerde = hex(verde).replace('0x','')
    if len(hexVerde) < 2: hexVerde = '0'+hexVerde
    hexAzul = hex(azul).replace('0x','')
    if len(hexAzul) < 2: hexAzul = '0'+hexAzul
    return "#%s%s%s" % (hexRojo, hexVerde, hexAzul)





# Comandos:

def config(ip, puerto):
    '''
    Crea o modifica el archivo de configuración
    '''
    
    try:    # Caso 1: ya existe el archivo LEDino.cfg
        with open("/Users/valen/Codigo/LEDino/LEDino.cfg", 'r') as config:

            ipDoc = config.readline()
            puertoDoc = config.readline()

            if not ip and not puerto:
                print("ip: %spuerto: %s" % (ipDoc, puertoDoc))
            
            else:
                if ip:
                    ipDoc = ip + '\n'
                if puerto:
                    puertoDoc = puerto
        
        if ip or puerto:
            with open("/Users/valen/Codigo/LEDino/LEDino.cfg", 'w') as config:
                config.write(ipDoc + puertoDoc)

    except FileNotFoundError:   # Caso 2: no existe el archivo, entonces lo creamos
        crearConfig()



def color(color):
    '''
    Cambia el color del LED
    '''

    # Determina el mensaje para enviar al aurduino
    
    if color == 'rojo':
        mensaje = '255:0:0'
    elif color == 'verde':
        mensaje = '0:255:0'
    elif color == 'azul':
        mensaje = '0:0:255'
    elif color == 'apagado' or color == 'negro':
        mensaje = '0:0:0'
    elif color == 'blanco':
        mensaje = '255:255:255'

    elif validarColor(color):
        mensaje = color

    else:
        print("Ingrese 'rojo', 'verde', 'azul' o un color en formato 'r:g:b'")
        print("donde r, g y b son los canales para rojo verde y azul respectivamente.")
        print("Los valores de r, g, b deben ser un entero entre 0-255 inclusive.")
        return

    mensaje = 'c' + mensaje

    # Envia el mensaje
    enviarMensaje(mensaje)


def parpadear(estado):
    '''
    Determina si el LED parpadea
    '''

    if estado == "ence":
        mensaje = 'pe'
    elif estado == "apag":
        mensaje = 'pa'
    elif estado == "camb":
        mensaje = 'pc'

    enviarMensaje(mensaje)