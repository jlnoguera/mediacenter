import json


class Menu:
    
    '''
        Constructor por defecto
    '''
    def __init__(self):
        self.datos =[] 

        try:
            with open('menu.json') as datos:
                self.datos = json.load(datos)

        except: 
            self.datos =[] 


    '''
    Carga el vector datos con un json para las opciones de menu

    params : jsonDatos recibe un json con las opciones de menu
    '''
    def JsonDatos(self,jsonDatos):
        self.datos = jsonDatos

   #Devuelve las opciones de menu disponibles
    def Opciones(self):
        return self.datos
