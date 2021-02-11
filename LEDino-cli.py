"""
Wrapper para la aplicación de linea de comandos
"""

import click
import LEDino


# Comando principal

@click.group()
def ledino():
    pass

# Subcomandos:

@ledino.command()
@click.option('--ip', default = None)
@click.option('--puerto', default = None)
def config(ip, puerto):
    '''
    Crea o modifica el archivo de configuración
    '''
    LEDino.config(ip, puerto)
    



@ledino.command()
@click.argument('color')
def color(color):
    '''
    Cambia el color del LED
    '''
    LEDino.color(color)


@ledino.command()
@click.argument('estado', default="camb",  type=click.Choice(["ence", "apag", "camb"], case_sensitive=False))
def parpadear(estado):
    '''
    Determina si el LED parpadea
    '''
    LEDino.parpadear(estado)