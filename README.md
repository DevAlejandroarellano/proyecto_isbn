# Proyecto Validador ISBN

[![Pruebas y Cobertura](https://github.com/DevAlejandroarellano/proyecto_isbn/actions/workflows/ci.yml/badge.svg)](https://github.com/DevAlejandroarellano/proyecto_isbn/actions)

Este proyecto es una implementación de un validador de ISBN (ISBN-10 e ISBN-13) en Python, desarrollado como parte de una actividad de Pruebas de Software. Incluye una suite de pruebas unitarias robusta que alcanza el 100% de cobertura de líneas y ramas, pruebas *property-based* con Hypothesis, y una pipeline de Integración Continua (CI/CD) con GitHub Actions.

## Características

* Validación de **ISBN-10** (incluyendo dígito de control 'X').
* Validación de **ISBN-13** (algoritmo de suma ponderada 1 y 3).
* Función de **limpieza** que elimina guiones y espacios.
* Función de **detección** automática (ISBN-10, ISBN-13, o Inválido).

## Instalación y Entorno

1.  Clona el repositorio:
    ```bash
    git clone [https://github.com/DevAlejandroarellano/proyecto_isbn.git](https://github.com/DevAlejandroarellano/proyecto_isbn.git)
    cd proyecto_isbn
    ```
2.  Instala las dependencias de desarrollo:
    ```bash
    pip install pytest pytest-cov hypothesis
    ```

## Ejecución de Pruebas y Cobertura

Para ejecutar la suite de pruebas completa (19 tests) y generar el reporte de cobertura en la terminal, utiliza el siguiente comando:

```bash
python -m pytest --cov=src