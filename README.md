<<<<<<< HEAD
Sistema de Gestión Hospitalaria
Descripción

Sistema de gestión hospitalaria desarrollado en Python con Programación Orientada a Objetos (POO). Permite administrar pacientes, doctores y citas médicas mediante una interfaz de consola.

Requisitos previos

Antes de ejecutar el proyecto asegúrate de tener instalado:

Python 3.10 o superior
pip (gestor de paquetes)
Git (opcional)

Instalación del proyecto
1. Clonar el repositorio
git clone https://github.com/tu_usuario/tu_repositorio.git
2. Entrar al proyecto
cd tu_repositorio
Crear entorno virtual (recomendado)
Windows:
python -m venv venv
venv\Scripts\activate
Mac / Linux:
python3 -m venv venv
source venv/bin/activate
Instalación de dependencias

Si tienes requirements.txt:

pip install -r requirements.txt

Si no lo tienes, puedes instalar manualmente:

pip install sqlalchemy
Inicializar base de datos

Ejecuta el siguiente archivo para crear las tablas:

python main.py

(El sistema inicializa automáticamente la base de datos al ejecutarse)

Ejecutar el proyecto
python main.py

Funcionalidades
Registrar pacientes
Registrar doctores
Agendar citas médicas
Consultar pacientes
Consultar doctores
Consultar citas

Autor

Proyecto desarrollado como parte de una prueba técnica de desarrollo backend en Python.

Notas finales
El sistema funciona desde consola
Usa SQLAlchemy como ORM
Implementa arquitectura por capas (models / services / database)
=======
# Proyecto_Hospital
Este proyecto corresponde a una prueba técnica de desarrollo de software orientada al perfil Python / Backend.
>>>>>>> 83e221ed8fd22fb219d7b4cd89c994b232cca4f4
