import psycopg2
from datetime import datetime, timedelta

class CitaService:

    @staticmethod
    def get_connection():
        return psycopg2.connect(
            host="localhost",
            database="hospital_db",
            user="postgres",
            password="postgres123"
        )

    @staticmethod
    def validar_cita(doctor_id, fecha_cita):

        conn = CitaService.get_connection()
        cursor = conn.cursor()

        ahora = datetime.now()

        # =========================
        # 0. NO CITAS EN EL PASADO NI MENOS DE 1 HORA
        # =========================
        if fecha_cita < ahora + timedelta(hours=1):
            conn.close()
            return False, "La cita debe ser al menos 1 hora en el futuro"

        # =========================
        # 1. HORARIO LABORAL (09:00 - 20:30)
        # =========================
        hora_inicio = 9
        hora_fin = 20

        if fecha_cita.hour < hora_inicio or fecha_cita.hour > hora_fin:
            conn.close()
            return False, "Fuera de horario laboral (09:00 - 20:30)"

        # caso especial: 20:30 permitido, pero no más tarde
        if fecha_cita.hour == 20 and fecha_cita.minute > 30:
            conn.close()
            return False, "Última cita permitida: 20:30"

        # =========================
        # 2. SOLO BLOQUES DE 30 MIN
        # =========================
        if fecha_cita.minute not in [0, 30]:
            conn.close()
            return False, "Solo se permiten citas cada 30 minutos (00 o 30)"

        # =========================
        # 3. CONFLICTO DE CITA (MISMO DOCTOR MISMO HORARIO)
        # =========================
        cursor.execute("""
            SELECT 1 FROM citas
            WHERE doctor_id = %s
            AND fecha_cita = %s
        """, (doctor_id, fecha_cita))

        if cursor.fetchone():
            conn.close()
            return False, "El doctor ya tiene una cita en ese horario"

        conn.close()
        return True, "OK"

    @staticmethod
    def crear_cita(paciente_id, doctor_id, fecha_cita):

        valido, mensaje = CitaService.validar_cita(doctor_id, fecha_cita)

        if not valido:
            return mensaje

        conn = CitaService.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO citas (paciente_id, doctor_id, fecha_cita)
            VALUES (%s, %s, %s)
        """, (paciente_id, doctor_id, fecha_cita))

        conn.commit()
        conn.close()

        return "Cita registrada correctamente"
    @staticmethod
    def obtener_citas():
        conn = CitaService.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM citas")
        citas = cursor.fetchall()

        conn.close()
        return citas