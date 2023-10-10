class Direccion:
    Derecha=Direccion("Derecha",0,1,0)
    Arriba=Direccion("Arriba",1,0,1)
    Izquierda=Direccion("Izquierda",2,-1,0)
    Abajo=Direccion("Abajo",3,0,-1)
    direcciones={
        "derecha":Derecha,
        "arriba":Arriba,
        "izquierda":Izquierda,
        "abajo":Abajo
    }
    def __init__(self, nombre, valor,dx,dy):
        self.valor=valor
        self.nombre=nombre
        self.dx=dx
        self.dy=dy
    
    def textoADireccion(text):
        if(text[0]!= None):
            return direcciones[text.lower()]
        else:
            return text
        