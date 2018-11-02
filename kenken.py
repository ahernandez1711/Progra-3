
"""
Programa 2: KenKen
Elaborado por: Daniel Pantigoso Valladares, Andrés Hernández y Juan Pablo
Fecha de creación: 05-10-2018
Fecha de última modificación: 12-10-2018

Notas para pensar:
1.
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

        for F in (ventanaPrincipal, Top10): #F mayuscula para indicar que son los Frames
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
        tk.Frame.geometry('500x200')

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
                                      command = None)\
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
        
        
        

"""class iniciarJuego(tk.Frame):

class otroJuego(tk.Frame):

class reiniciarJuego(tk.Frame):

class terminarJuego(tk.Frame):"""

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
        botonVolver = tk.Button(self, text = "Volver al juego", font = BODY_FONT, bg = "yellow",\
                                   command = lambda: controller.show_frame(ventanaPrincipal))\
                                   .grid(row = 13, column = 1, padx = 2, pady = 2)        
        
        boton1=tk.Button(self, bg='yellow')
        boton2=tk.Button(self,bg='red')
        boton3=tk.Button(self,bg='blue')
        boton4=tk.Button(self,bg='green')
        boton5=tk.
        boton6
        boton7
        boton8
        boton9
   
        
        
    
    
        
"""Fin de clases."""
#Programa Principal
aplicacion = KenKen()
aplicacion.mainloop()
