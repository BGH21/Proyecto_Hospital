class Doctor:
    def __init__(self, id, nombre, especialidad):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return (
            f"Doctor("
            f"id={self.id}, "
            f"nombre={self.nombre}, "
            f"especialidad={self.especialidad}"
            f")"
        )

    def __repr__(self):
        return self.__str__()