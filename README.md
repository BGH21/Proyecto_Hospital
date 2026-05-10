# Sistema de Gestión Hospitalaria

Proyecto desarrollado en Python utilizando PostgreSQL.

El sistema permite administrar pacientes, doctores y citas médicas mediante una aplicación de consola.

---

# Funcionalidades

- Registrar pacientes
- Registrar doctores
- Registrar citas médicas
- Visualizar pacientes registrados
- Visualizar doctores registrados
- Visualizar citas registradas
- Consultar citas de un paciente específico
- Validar conflictos de horarios en citas
- Restricción de horario laboral

---

# Tecnologías utilizadas

- Python 3
- PostgreSQL
- psycopg2

---

# Requisitos previos

Antes de ejecutar el proyecto debes tener instalado:

- Python 3.10 o superior
- PostgreSQL
- pip

---

# Instalación del proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/BGH21/Proyecto_Hospital.git
```

## 2. Entrar al proyecto

```bash
cd Proyecto_Hospital
```

---

# Crear entorno virtual (Opcional)

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Instalar dependencias

```bash
pip install psycopg2
```

---

# Configuración de PostgreSQL

## 1. Crear la base de datos

Entrar a PostgreSQL:

```sql
psql -U postgres
```

Crear la base de datos:

```sql
CREATE DATABASE hospital_db;
```

Conectarse a la base de datos:

```sql
\c hospital_db
```

---

## 2. Ejecutar el archivo SQL

Dentro de PostgreSQL ejecutar:

```sql
\i 'RUTA_DEL_PROYECTO/sql/database.sql'
```

Ejemplo en Windows:

```sql
\i 'C:/Users/usuario/Desktop/Proyecto_Hospital/sql/database.sql'
```

Esto creará las tablas y cargará datos iniciales.

---

# Configurar conexión a PostgreSQL

Modificar las credenciales en:

- `paciente_service.py`
- `doctor_service.py`
- `cita_service.py`

```python
host="localhost",
database="hospital_db",
user="postgres",
password="TU_PASSWORD"
```

---

# Ejecutar el proyecto

```bash
python main.py
```

---

# Estructura del proyecto

```text
Proyecto_Hospital/
│
├── app/
│   ├── models/
│   ├── services/
│   └── database/
│
├── sql/
│   └── database.sql
│
├── main.py
├── README.md
```

---

# Autor
Belen Gaytan Herrera