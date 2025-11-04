# Plan de pruebas — Validador de ISBN

## 1. Objetivo
Comprobar que las funciones del archivo "isbn.py" funcionan correctamente para reconocer si un número ISBN-10 o ISBN-13 es válido o no.

## 2. Qué se va a probar
Se van a probar estas funciones:
- normalize_isbn: limpia el texto quitando guiones y espacios.
- is_valid_isbn10: revisa si un número es un ISBN-10 correcto.
- is_valid_isbn13: revisa si un número es un ISBN-13 correcto.
- detect_isbn: dice si el número es ISBN-10, ISBN-13 o inválido.

## 3. Qué se supone
- El usuario siempre va a escribir una cadena.
- No se usan librerías externas, solo código propio.
- Las funciones siempre dan el mismo resultado con la misma entrada.

## 4. Riesgos o posibles errores
- Que el cálculo del número de control (checksum) esté mal.
- Que no se prueben todos los casos con “X”.
- Que las funciones fallen con caracteres raros o vacíos.

## 5. Casos de prueba
- Pruebas para ISBN-10

1. Se probará un número ISBN-10 normal: “0-306-40615-2”.
Se espera que el programa lo reconozca como válido.

2. Se probará un número ISBN-10 con una “X” al final: “0-8044-2957-X”.
Se espera que sea válido, ya que la “X” representa el número 10.

3. Se probará un ISBN-10 con error en el número de control: “0-306-40615-3”.
Se espera que el programa lo marque como inválido.

4. Se probará un ISBN-10 con menos de 10 dígitos: “123456789”.
Se espera que sea inválido, por tener una longitud incorrecta.

5. Se probará un ISBN-10 con la letra “x” minúscula al final: “080442957x”.
Se espera que sea válido, reconociendo la letra minúscula como “X”.

6. Se probará un ISBN-10 con una letra en medio del número: “0-306-4061A-2”.
Se espera que sea inválido, ya que contiene un carácter no permitido.

7. Se probará un ISBN-10 con una letra al final que no es “X”: “123456789Z”.
Se espera que sea inválido.
Esta prueba servirá para cubrir el caso donde el último carácter no sea válido.

- Pruebas para ISBN-13

1. Se probará un ISBN-13 correcto: “9780306406157”.
Se espera que el programa lo reconozca como válido.

2. Se probará un ISBN-13 con el último dígito incorrecto: “9780306406158”.
Se espera que sea inválido, por error en el número de control.

3. Se probará un ISBN-13 con más de 13 dígitos: “12345678901234”.
Se espera que sea inválido, ya que la longitud es demasiado grande.

4. Se probará un ISBN-13 con una letra en el número: “97803064A6157”.
Se espera que sea inválido, por contener un carácter que no es un número.

5. Se probará un ISBN-13 con solo 12 dígitos: “123456789012”.
Se espera que sea inválido, por ser demasiado corto.

- Pruebas para limpiar el ISBN

1. Se probará la función con un valor nulo (None).
Se espera que devuelva una cadena vacía.

2. Se probará con una cadena que contenga muchos espacios y guiones: “ 978- 0- 3064-06 15- 7 x ”.
Se espera que el resultado sea “9780306406157X”, es decir, el número limpio y en mayúsculas.

- Pruebas para detectar el tipo de ISBN

1. Se probará la función con un ISBN-10: “0-306-40615-2”.
Se espera que el resultado indique que es un ISBN-10.

2. Se probará la función con un ISBN-13: “9780306406157”.
Se espera que el resultado indique que es un ISBN-13.

3. Se probará la función con un número que no cumpla las reglas de ningún tipo: “1234567890”.
Se espera que el programa lo marque como Inválido.

## 6. Casos en los límites
- ISBN-10 con 9, 10 y 11 dígitos.
- ISBN-13 con 12, 13 y 14 dígitos.
- Cadena vacía o valor nulo (None).

## 7. Qué se espera lograr
- Tener una cobertura del código de al menos 90% de líneas y 85% de ramas.
- Asegurar que las funciones respondan bien con datos válidos e inválidos.

## 8. Cómo se harán las pruebas
- Se usarán pruebas automáticas con pytest.
- Se probarán casos normales (caja negra) y casos internos (caja blanca).
- Se hará una prueba especial con un “doble” (función simulada) para verificar una parte del código.
