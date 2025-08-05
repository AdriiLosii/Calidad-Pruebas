def a2r(number):
    """
    Convierte un número arábigo (entero) a un número romano (cadena).
    """
    if number <= 0 or number > 3000:
        raise ValueError("El número debe estar entre 1 y 3000.")

    if type(number)!=int:
        raise ValueError("El número debe de ser un entero")

    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    resultado = []
    for valor, simbolo in valores:
        while number >= valor:
            resultado.append(simbolo)
            number -= valor
    return ''.join(resultado)


def r2a(roman):
    """
    Convierte un número romano (cadena) a un número arábigo (entero).
    """
    valores = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400,
        "C": 100, "XC": 90, "L": 50, "XL": 40,
        "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
    }

    total = 0
    prev_value = 0
    for char in roman:
        if char not in valores:
            raise ValueError(f"Símbolo romano inválido: {char}")
        current_value = valores[char]
        if current_value > prev_value:
            # Caso especial: resta
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value

    # Validación de secuencia
    if a2r(total) != roman:
        raise ValueError("La secuencia de números romanos no es válida.")
    return total