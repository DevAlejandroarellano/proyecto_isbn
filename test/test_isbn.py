# test/test_isbn.py

# Importaciones de funciones de negocio
from src.isbn import es_isbn10_valido, es_isbn13_valido, tipo_isbn, limpiar_isbn
# Importación clave para Hypothesis (soluciona el NameError)
from hypothesis import given, strategies as st 

# ----------------------------
# Pruebas Unitarias (100% de cobertura)
# ----------------------------

# PRUEBAS PARA ISBN-10
def test_isbn10_valido_normal():
    assert es_isbn10_valido("0-306-40615-2") == True

def test_isbn10_valido_con_X():
    assert es_isbn10_valido("0-8044-2957-X") == True

def test_isbn10_invalido_por_checksum():
    assert es_isbn10_valido("0-306-40615-3") == False

def test_isbn10_invalido_por_longitud_corta():
    assert es_isbn10_valido("123456789") == False

def test_isbn10_valido_con_x_minuscula():
    assert es_isbn10_valido("080442957x") == True 

def test_isbn10_invalido_caracter_ilegal_medio():
    assert es_isbn10_valido("0-306-4061A-2") == False 

def test_isbn10_invalido_caracter_ilegal_final_no_X():
    # Este test cubrió el último gap de cobertura
    assert es_isbn10_valido("123456789Z") == False

# PRUEBAS PARA ISBN-13
def test_isbn13_valido_normal():
    assert es_isbn13_valido("9780306406157") == True

def test_isbn13_invalido_por_digito():
    assert es_isbn13_valido("9780306406158") == False

def test_isbn13_invalido_por_longitud_larga():
    assert es_isbn13_valido("12345678901234") == False

def test_isbn13_invalido_por_letra():
    assert es_isbn13_valido("97803064A6157") == False

def test_isbn13_invalido_longitud_corta():
    assert es_isbn13_valido("123456789012") == False

# PRUEBAS PARA limpiar_isbn
def test_limpiar_isbn_entrada_nula():
    assert limpiar_isbn(None) == ""

def test_limpiar_isbn_frontera_compleja():
    assert limpiar_isbn("  978- 0- 3064-06 15- 7 x ") == "9780306406157X"

# PRUEBAS PARA detectar tipo
def test_detecta_isbn10():
    assert tipo_isbn("0-306-40615-2") == "ISBN-10"

def test_detecta_isbn13():
    assert tipo_isbn("9780306406157") == "ISBN-13"

def test_detecta_invalido():
    assert tipo_isbn("1234567890") == "Inválido"

# ----------------------------
# Pruebas Property-Based (Hypothesis)
# ----------------------------

# Propiedad 1: Idempotencia de la limpieza (limpiar dos veces es igual a limpiar una)
@given(st.text(min_size=0, max_size=50))
def test_propiedad_limpieza_es_idempotente(codigo):
    limpio_una_vez = limpiar_isbn(codigo)
    limpio_dos_veces = limpiar_isbn(limpio_una_vez)
    assert limpio_una_vez == limpio_dos_veces

# Propiedad 2: Invarianza de la validez ante la presencia de formato simple (guiones)
@given(st.text(alphabet=st.characters(min_codepoint=48, max_codepoint=57), min_size=13, max_size=13))
def test_propiedad_validez_isbn13_invariante_a_guiones(codigo_sin_guiones):
    # Esta prueba asegura que la función limpiar_isbn() del SUT maneja el formato sin romper la validez
    if es_isbn13_valido(codigo_sin_guiones):
        codigo_con_guiones = codigo_sin_guiones[:3] + "-" + codigo_sin_guiones[3:]
        assert es_isbn13_valido(codigo_con_guiones) == True