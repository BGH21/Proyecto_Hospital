from datetime import datetime

from app.database.init_db import init_db

from app.sevices.paciente_service import PacienteService
from app.sevices.doctor_service import DoctorService        
from app.sevices.cita_service import CitaService

def mostrar_menu():
    print("\n===== SISTEMA HOSPITALARIO =====")
    print("1. Registrar paciente")
    print("2. Registrar doctor")
    print("3. Registrar cita")
    print("4. Ver pacientes")
    print("5. Ver doctores")
    print("6. Ver citas")
    print("7. Salir")


def registrar_paciente():
    nombre = input("Nombre del paciente: ")
    sintomas = input("Síntomas: ")

    paciente = PacienteService.crear_paciente(
        nombre,
        sintomas
    )

    print("\nPaciente registrado correctamente")
    print(paciente)


def registrar_doctor():
    nombre = input("Nombre del doctor: ")
    especialidad = input("Especialidad: ")

    doctor = DoctorService.crear_doctor(
        nombre,
        especialidad
    )

    print("\nDoctor registrado correctamente")
    print(doctor)


def registrar_cita():
    paciente_id = int(input("ID del paciente: "))
    doctor_id = int(input("ID del doctor: "))

    fecha = input(
        "Fecha y hora "
        "(YYYY-MM-DD HH:MM): "
    )

    fecha_cita = datetime.strptime(
        fecha,
        "%Y-%m-%d %H:%M"
    )

    resultado = CitaService.crear_cita(
    paciente_id,
    doctor_id,
    fecha_cita
    )

    print("\n" + resultado)


def ver_pacientes():
    pacientes = PacienteService.obtener_pacientes()

    print("\n===== PACIENTES =====")

    for paciente in pacientes:
        print(paciente)


def ver_doctores():
    doctores = DoctorService.obtener_doctores()

    print("\n===== DOCTORES =====")

    for doctor in doctores:
        print(doctor)


def ver_citas():
    citas = CitaService.obtener_citas()

    print("\n===== CITAS =====")

    for cita in citas:
        print(cita)


def main():
    init_db()

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_paciente()

        elif opcion == "2":
            registrar_doctor()

        elif opcion == "3":
            registrar_cita()

        elif opcion == "4":
            ver_pacientes()

        elif opcion == "5":
            ver_doctores()

        elif opcion == "6":
            ver_citas()

        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpción inválida")


if __name__ == "__main__":
    main()