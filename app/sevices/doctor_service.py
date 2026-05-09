import psycopg2

class DoctorService:

    @staticmethod
    def get_connection():
        return psycopg2.connect(
            host="localhost",
            database="hospital_db",
            user="postgres",
            password="postgres123"
        )

    @staticmethod
    def crear_doctor(nombre, especialidad):
        conn = DoctorService.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO doctores (nombre, especialidad)
            VALUES (%s, %s)
        """, (nombre, especialidad))

        conn.commit()
        conn.close()

        return "Doctor registrado correctamente"

    @staticmethod
    def obtener_doctores():
        conn = DoctorService.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM doctores")
        doctores = cursor.fetchall()

        conn.close()
        return doctores