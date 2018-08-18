
class Menu:
    """Clase para la logica de menus de opciones de la aplicacion
       Control de pulsacion de teclas par navegar por las opciones de menu
       y selección de estas.
       Una vez seleccionadas, lanzamiento de la opción para ejecutarse.
    """
    def __init__(self):
        self.datos =[]  

    def JsonDatos(self,jsonDatos):
        self.datos = jsonDatos