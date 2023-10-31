def generar_contrasenia(self):
        import random
        import string

        self._contrasenia_matriculacion = "".join(
            random.choices(string.ascii_letters + string.digits, k=6)
        )