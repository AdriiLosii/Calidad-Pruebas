def es_dni(data):
    def _letra(n):
        try:
            return "TRWAGMYFPDXBNJZSQVHLCKE"[n % 23]
        except IndexError:
            return ""

    def _control(txt):
        T = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        w, wi, r = [7, 3, 1], 0, 0
        for i in txt:
            if "0" <= i <= "9":
                # Dígito
                r += w[wi] * int(i)
                wi = (wi + 1) % 3
            elif i in T:
                # Letra
                r += w[wi] * (T.index(i) + 10)
                wi = (wi + 1) % 3
        return str(r % 10)

    # MODIFICACIÓN: Asegurarnos de que la longitud es la correcta
    if len(data) < 60:
        raise ValueError(f"Longitud de texto insuficiente: esperado al menos 60, recibido: {len(data)}")

    # Validar primera parte (IDESP + soporte + control)
    if data[:5] != "IDESP":
        return False
    if _control(data[5:14]) != data[14]:
        return False

    # Validar número NIF y letra de control
    try:
        nif_number = int(data[15:23])
        if _letra(nif_number) != data[23]:
            return False
    except ValueError:
        return False

    # Validar fecha de nacimiento
    if _control(data[30:36]) != data[36]:
        return False

    # Validar fecha de expiración
    if _control(data[38:44]) != data[44]:
        return False

    # Validar genérico
    combined_fields = data[5:14] + data[14] + data[15:23] + data[23] + data[30:36] + data[36] + data[38:44] + data[44]
    if _control(combined_fields) != data[59]:
        return False

    return True
