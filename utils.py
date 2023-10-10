def limpiar_terminal():
    print(chr(27) + "[2J")

def validar_celda(celda="a2", max_col= 'D', max_row= 4):
    # Implementa la lógica de validación de celda aquí
    if len(celda) != 2:
        return False
    col,row = celda[0].upper(), celda[1]
    valido = 'A' <= col<= max_col and '1'<= row <= str(max_row)
    return valido


def comprobar_celda_disponible(celda, equipo):
     for p in equipo:
         if(p.posicion == celda ):
            print("Celda ocupada. Por favor, elija otra celda.")
            continue

def validar_celda_contigua(celda1, celda2):
    # Implementa la lógica de validación de celda contigua aquí
    pass

