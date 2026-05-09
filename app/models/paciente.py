class Paciente:
    def __init__(self, id, nombre, sintomas):
        self.id = id
        self.nombre = nombre
        self.sintomas = sintomas

    def __str__(self):
        return (
            f"Paciente("
            f"id={self.id}, "
            f"nombre={self.nombre}, "
            f"sintomas={self.sintomas}"
            f")"
        )

    def __repr__(self):
        return self.__str__()