CREATE TABLE pacientes (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    sintomas TEXT NOT NULL
);

CREATE TABLE doctores (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    especialidad TEXT NOT NULL
);

CREATE TABLE citas (
    id SERIAL PRIMARY KEY,
    doctor_id INTEGER NOT NULL,
    paciente_id INTEGER NOT NULL,
    fecha_cita TIMESTAMP NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctores(id),
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

INSERT INTO pacientes (nombre, sintomas)
VALUES ('Maria Lopez', 'Dolor de cabeza');

INSERT INTO pacientes (nombre, sintomas)
VALUES ('Juan Perez', 'Fiebre y tos');

INSERT INTO pacientes (nombre, sintomas)
VALUES ('Ana Torres', 'Dolor abdominal');

INSERT INTO pacientes (nombre, sintomas)
VALUES ('Carlos Mendez', 'Mareos frecuentes');

INSERT INTO pacientes (nombre, sintomas)
VALUES ('Sofia Ramirez', 'Dolor de garganta');

INSERT INTO pacientes (nombre, sintomas)
VALUES ('Luis Hernandez', 'Fatiga y debilidad');

INSERT INTO doctores (nombre, especialidad)
VALUES ('Dr. Ramirez', 'Cardiología');

INSERT INTO doctores (nombre, especialidad)
VALUES ('Dra. Martinez', 'Pediatría');

INSERT INTO doctores (nombre, especialidad)
VALUES ('Dr. Gomez', 'Medicina General');

INSERT INTO doctores (nombre, especialidad)
VALUES ('Dra. Lopez', 'Dermatología');

INSERT INTO doctores (nombre, especialidad)
VALUES ('Dr. Sanchez', 'Neurología');

INSERT INTO doctores (nombre, especialidad)
VALUES ('Dra. Vargas', 'Ginecología');

INSERT INTO citas (doctor_id, paciente_id, fecha_cita)
VALUES (1, 1, '2026-05-10 09:00:00');