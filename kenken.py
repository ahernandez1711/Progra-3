"""
Programa 2: KenKen
Elaborado por: Daniel Pantigoso Valladares, Andrés Hernández y Juan Pablo
Fecha de creación: 05-10-2018
Fecha de última modificación: 6-11-2018
"""

#Importa módulos
from tkinter import messagebox
from tkinter import ttk
import os #Para el filepath del archivo.
import pickle #Para no convertir tipos de datos cuando abrimos archivos.
import time #Para el timer.
import tkinter as tk
import tkinter.filedialog #Para abrir documentos.

"""Empiezan las funciones/variables generales:"""
#Variables
KenKen = ("Fixedsys", 32, "bold")
top10Font = ("Arial", 10, "bold underline")
BODY_FONT = ("Verdana", 10)
BODY_FONT_ITALIC = ("Verdana", 10, "italic")
BODY_FONT_BOLD = ("Verdana", 10, "bold")

def salir(event = None):
   quit()

#Abre ventana de "Acerca de".
def abreAcercaDe():
    messagebox.showinfo("Información general", "Nombre del programa: KenKen.\n"
    "Fecha de creación: 05 de octubre del 2018.\n"
    "Fecha de última modificación: 12 de octubre del 2018.\n"
    "Autores del programa: Daniel Pantigoso, Andrés Hernández y Juan Pablo Vargas")

def validarJuego():
    print("Todavia no esta lista esta funcion")
    messagebox.showinfo("HAY ERRORES EN EL JUEGO")

def botonesTablero(numeroDeCasillas):
    fila = []
    columna =[]
    for i in range (numeroDeCasillas):
        fila.append(columna)
        for j in fila:
            columna.append([str(i)])
    return fila

"""Fin de las funciones/variables generales."""

"""Empiezan clases:"""
class KenKen(tk.Tk): #Clase principal
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #Initialize
        
        tk.Tk.iconbitmap(self, "Monogatari Araragi - OOMPH.ico")
        tk.Tk.wm_title(self, "Proyecto de programación 2: KenKen")
        
        #Container
        container = tk.Frame(self)
        container.grid()
        container.grid_rowconfigure(0, weight = 1) #Row Configure
        container.grid_columnconfigure(0, weight = 1) #Column configure

        self.frames = {}

        for F in (ventanaPrincipal, Top10, IniciarJuego): #F mayuscula para indicar que son los Frames
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 12, column = 12, sticky = "NESW", padx = 1, pady = 1)
        
        self.show_frame(ventanaPrincipal)

    def show_frame(self, contenedor):
        frame = self.frames[contenedor]
        frame.tkraise()

#Ventana principal, esta es la base de todas, el "menú".
class ventanaPrincipal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Row Configure
        tk.Frame().grid_rowconfigure(0, weight = 1)

        #Column configure
        tk.Frame().grid_columnconfigure(0, weight = 1)

        #Labels
        labelKenKen = tk.Label(self, text = "KEN KEN", font = KenKen)\
                .grid(row = 0, rowspan = 2, column = 5, columnspan = 3, padx = 5, pady = 5, sticky = "NESW")
        labelHoras = tk.Label(self, text = "Horas")\
                .grid(row = 0, column = 10, sticky = "NESW")
        labelMinutos = tk.Label(self, text = "Minutos")\
                .grid(row = 0, column = 11, sticky = "NESW")
        labelSegundos = tk.Label(self, text = "Segundos")\
                .grid(row = 0, column = 12, sticky = "NESW")
        

        #Botones
        botonPausa = tk.Button(self, text = "PAUSA", font = BODY_FONT, bg = "peru",\
                               command = None)\
                               .grid(row = 3, column = 12, padx = 1, pady = 1, sticky = "NESW")
        
        botonIniciarJuego = tk.Button(self, text = "INICIAR JUEGO", font = BODY_FONT, bg = "red",\
                                      command = lambda: controller.show_frame(IniciarJuego))\
                                      .grid(row = 10, column = 0,  padx = 1, pady = 1, sticky = "NESW")
        
        botonValidarJuego = tk.Button(self, text = "VALIDAR JUEGO", font = BODY_FONT,\
                                      bg = "green", command = lambda: validarJuego)\
                                      .grid(row = 10, column = 2,  padx = 1, pady = 1, sticky = "NESW")
        
        botonOtroJuego = tk.Button(self, text = "OTRO JUEGO", font = BODY_FONT, bg = "light blue",\
                                   command = None)\
                                   .grid(row = 10, column = 4,  padx = 1, pady = 1)
        botonReiniciarJuego = tk.Button(self, text = "REINICIAR JUEGO", font = BODY_FONT, bg = "orange",\
                                        command = None)\
                                        .grid(row = 10, column = 6,  padx = 1, pady = 1, sticky = "NESW")
        
        botonTerminarJuego = tk.Button(self, text = "TERMINAR JUEGO", font = BODY_FONT, bg = "pink",\
                                       command = None)\
                                       .grid(row = 10, column = 8,  padx = 1, pady = 1, sticky = "NESW")
        
        botonTop10 = tk.Button(self, text = "TOP 10", font = BODY_FONT, bg = "light green",\
                               command = lambda: controller.show_frame(Top10))\
                               .grid(row = 12, column = 8,  padx = 1, pady = 1, sticky = "NESW")
        
        
        

class IniciarJuego(tk.Frame):
    def __init__(self, parent, controller):
        v = tk.IntVar() #Valor para el formato de las casillas
        v.set(1) #El default para 3x3
        d = tk.IntVar() #Valor para la dificultad del juego
        d.set(1) #El default para Principiante
        
        tk.Frame.__init__(self, parent)
        
        #Labels
        labelEscogerCasillas = tk.Label(self, text = "Escoja el formato: ", font = BODY_FONT_BOLD)
        labelEscogerCasillas.grid(row = 0, column = 0, padx = 2, pady = 2)
        
        labelEscogerDificultad = tk.Label(self, text = "Escoja la dificultad: ", font = BODY_FONT_BOLD)

        labelEscogerDificultad.grid(row = 0, column = 4, padx = 2, pady = 2)
        
        
        #Botones
        #Formato
        formatos = [("3x3", 1), ("4x4", 2), ("5x5", 3), ("6x6", 4), ("7x7", 5), ("8x8", 6), ("9x9", 7)]

        for valor, formato in enumerate(languages):
            tk.Radiobutton(aplicacion, text = language, padx = 20, variable = v, command = ShowChoice, value=val)\
                                       .grid()
        
        boton3x3 = tk.Radiobutton(self, text = "3 x 3", font = BODY_FONT, variable = v, value = 1)\
                                         .grid(row = 1, column = 0, padx = 1, pady = 1)

        boton4x4 = tk.Radiobutton(self, text = "4 x 4", font = BODY_FONT, variable = v, value = 2)\
                                         .grid(row = 2, column = 0, padx = 1, pady = 1)

        boton5x5 = tk.Radiobutton(self, text = "5 x 5", font = BODY_FONT, variable = v, value = 3)\
                                         .grid(row = 3, column = 0, padx = 1, pady = 1)

        boton6x6 = tk.Radiobutton(self, text = "6 x 6", font = BODY_FONT, variable = v, value = 4)\
                                         .grid(row = 4, column = 0, padx = 1, pady = 1)

        boton7x7 = tk.Radiobutton(self, text = "7 x 7", font = BODY_FONT, variable = v, value = 5)\
                                         .grid(row = 5, column = 0, padx = 1, pady = 1)

        boton8x8 = tk.Radiobutton(self, text = "8 x 8", font = BODY_FONT, variable = v, value = 6)\
                                         .grid(row = 6, column = 0, padx = 1, pady = 1)

        boton9x9 = tk.Radiobutton(self, text = "9 x 9", font = BODY_FONT, variable = v, value = 7)\
                                         .grid(row = 7, column = 0, padx = 1, pady = 1)
        
        #Dificultad
        dificultades = [("Principiante", 1), ("Intermedio", 2), ("Experto", 3)]
        botonPrincipiante = tk.Radiobutton(self, text = "Principiante", font = BODY_FONT, command = None)\
                                      .grid(row = 1, column = 4, padx = 1, pady = 1)
        botonIntermedio = tk.Radiobutton(self, text = "Intermedio", font = BODY_FONT, command = None)\
                                      .grid(row = 4, column = 4, padx = 1, pady = 1)
        botonDificil = tk.Radiobutton(self, text = "Experto", font = BODY_FONT, command = None)\
                                      .grid(row = 7, column = 4, padx = 1, pady = 1)
        
        botonVolver = tk.Button(self, text = "Volver al juego", font = BODY_FONT_BOLD, bg = "yellow",\
                                   command = lambda: controller.show_frame(ventanaPrincipal))\
                                   .grid(row = 13, column = 0, padx = 2, pady = 2)
"""
class OtroJuego(tk.Frame):
class ReiniciarJuego(tk.Frame):
class TerminarJuego(tk.Frame):"""

#Ventana de los tiempos de los mejores 10.
class Top10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Labels
        labelTop10 = tk.Label(self, text = "TOP 10", font = top10Font)
        labelNivel = tk.Label(self, text = "NIVEL", font = BODY_FONT_ITALIC)
        labelJugador = tk.Label(self, text = "JUGADOR", font = BODY_FONT_ITALIC)
        labelTiempo = tk.Label(self, text = "TIEMPO", font = BODY_FONT_ITALIC)

        labelTop10.grid(row = 0, column = 0, padx = 2, pady = 2)
        labelNivel.grid(row = 1, column = 0, padx = 2, pady = 2)
        labelJugador.grid(row = 1, column = 1, padx = 2, pady = 2)
        labelTiempo.grid(row = 1, column = 2, padx = 2, pady = 2)

        #Botones
        botonVolver = tk.Button(self, text = "Volver al juego", font = BODY_FONT_BOLD, bg = "yellow",\
                                   command = lambda: controller.show_frame(ventanaPrincipal))\
                                   .grid(row = 13, column = 1, padx = 2, pady = 2)
   
        
    
"""Fin de clases."""
#Programa Principal
aplicacion = KenKen()
aplicacion.mainloop()
