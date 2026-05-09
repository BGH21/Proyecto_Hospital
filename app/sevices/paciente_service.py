import psycopg2

class PacienteService:

    @staticmethod
    def get_connection():
        return psycopg2.connect(
            host="localhost",
            database="hospital_db",
            user="postgres",
            password="postgres123"
        )

    @staticmethod
    def crear_paciente(nombre, sintomas):
        conn = PacienteService.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO pacientes (nombre, sintomas)
            VALUES (%s, %s)
        """, (nombre, sintomas))

        conn.commit()
        conn.close()

        return "Paciente registrado correctamente"

    @staticmethod
    def obtener_pacientes():
        conn = PacienteService.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()

        conn.close()
        return pacientes