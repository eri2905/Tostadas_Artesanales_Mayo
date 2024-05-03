import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

import os
import tkinter as tk
from util.generic import leer_imagen

class MasterPanel:
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)            
        
        # Construir la ruta de la imagen del logo
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "imagenes", "logo.png")
        
        # Verificar si la imagen existe en la ruta especificada
        if not os.path.exists(image_path):
            print("Error: No se pudo encontrar la imagen del logo en la ruta especificada:", image_path)
            return
        
        # Cargar la imagen del logo
        logo = leer_imagen(image_path, (400, 250))
        
        # Verificar si la imagen se cargó correctamente
        if logo is None:
            print("Error: No se pudo cargar la imagen del logo")
            return
                        
        label = tk.Label(self.ventana, image=logo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana.mainloop()

if __name__ == "__main__":
    MasterPanel()
