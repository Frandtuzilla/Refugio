# Refugio

## Descripción
El proyecto **Refugio** es un sistema de gestión para refugios de animales. Permite registrar mascotas, adoptantes y adopciones, facilitando la administración de los procesos de adopción y el seguimiento de los animales en el refugio.

## Estructura del Proyecto
El proyecto está compuesto por las siguientes clases principales:

- **[`Mascota`](mascota.py):** Clase base para representar una mascota. Incluye atributos como nombre, ID, tipo, edad y disponibilidad.
- **[`Perro`](perro.py):** Subclase de `Mascota` que representa un perro. Incluye un atributo adicional para indicar si es lazarillo.
- **[`Gato`](gato.py):** Subclase de `Mascota` que representa un gato. Incluye un atributo adicional para definir su rasgo (sociable o solitario).
- **[`Pez`](pez.py):** Subclase de `Mascota` que representa un pez. Incluye un atributo adicional para indicar si es de agua dulce o salada.
- **[`Adoptante`](adoptante.py):** Clase que representa a una persona interesada en adoptar una mascota. Incluye atributos como nombre, DNI y la mascota adoptada.
- **[`Adopcion`](adopcion.py):** Clase que representa el proceso de adopción, relacionando un adoptante con una mascota y registrando la fecha de adopción.
- **[`Refugio`](refugio.py):** Clase principal que gestiona el refugio. Permite agregar, buscar y eliminar mascotas y adoptantes, así como registrar adopciones.

## Instalación
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
