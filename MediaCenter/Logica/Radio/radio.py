
import json

class Radio:
    
    """

    Author      : Jose Luis Noguera
    Date        : 20/08/2018
    Description : Clase para la reproducir radio por streaming

    """

  # Constructor por defecto 
    def __init__(self):
        self.jsonDatos =[]  

    def JsonDatos(self,jsonDatos):
        self.jsonDatos = json.load(jsonDatos)

   #Ejecuta las acciones definidas en self.jsonDatos 
    def Run(self):
        print self.jsonDatos["acciones"]
          

           

