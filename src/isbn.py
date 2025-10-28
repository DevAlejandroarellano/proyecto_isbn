# src/isbn.py

# ------------------------------
# Funciones para validar ISBN
# ------------------------------

#Nuevo comentario para CI

# Esta función quita espacios y guiones del texto
def limpiar_isbn(texto):
    if texto is None:
        return ""
    texto = texto.strip().replace("-", "").replace(" ", "")
    return texto.upper()

# Verifica si un ISBN-10 es válido
def es_isbn10_valido(codigo):
    codigo = limpiar_isbn(codigo)
    if len(codigo) != 10:
        return False
    
    total = 0
    for i in range(9):
        if not codigo[i].isdigit():
            return False
        total += int(codigo[i]) * (10 - i)

    # El último puede ser número o 'X'
    if codigo[9] == 'X':
        total += 10
    elif codigo[9].isdigit():
        total += int(codigo[9])
    else:
        return False

    return total % 11 == 0

# Verifica si un ISBN-13 es válido
def es_isbn13_valido(codigo):
    codigo = limpiar_isbn(codigo)
    if len(codigo) != 13 or not codigo.isdigit():
        return False
    
    total = 0
    for i in range(12):
        num = int(codigo[i])
        if i % 2 == 0:
            total += num
        else:
            total += num * 3
    
    digito_control = (10 - (total % 10)) % 10
    return digito_control == int(codigo[-1])

# Detecta qué tipo de ISBN es
def tipo_isbn(codigo):
    if es_isbn10_valido(codigo):
        return "ISBN-10"
    elif es_isbn13_valido(codigo):
        return "ISBN-13"
    else:
        return "Inválido"
