class Cita:
    def __init__(self, id, doctor_id, paciente_id, fecha_cita):
        self.id = id
        self.doctor_id = doctor_id
        self.paciente_id = paciente_id
        self.fecha_cita = fecha_cita

    def __str__(self):
        return (
            f"Cita("
            f"id={self.id}, "
            f"doctor_id={self.doctor_id}, "
            f"paciente_id={self.paciente_id}, "
            f"fecha_cita={self.fecha_cita}"
            f")"
        )