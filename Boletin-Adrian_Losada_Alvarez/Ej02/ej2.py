class Currency:
    """
    Clase base para representar una moneda y realizar operaciones básicas.
    """
    def __init__(self, symbol, amount):
        self.symbol = symbol
        if amount < 0:
            raise ValueError("La cantidad inicial no puede ser negativa.")
        self.amount = amount

    def suma(self, value):
        if value < 0:
            raise ValueError("No se puede agregar un valor negativo.")
        self.amount += value
        return self

    def resta(self, value):
        if value < 0:
            raise ValueError("No se puede restar un valor negativo.")
        self.amount -= value
        return self

    def multiplica(self, factor):
        if factor < 0:
            raise ValueError("El factor de multiplicación no puede ser negativo.")
        self.amount *= factor
        return self

    def mostrar(self):
        return f"{self.amount:.2f} {self.symbol}"


class Wallet:
    """
    Clase para gestionar una colección de monedas con operaciones básicas.
    """
    def __init__(self):
        self.balances = {}

    def suma(self, currency):
        if currency.symbol not in self.balances:
            self.balances[currency.symbol] = 0
        self.balances[currency.symbol] += currency.amount

    def resta(self, currency):
        if currency.symbol not in self.balances:
            self.balances[currency.symbol] = 0
        self.balances[currency.symbol] -= currency.amount

    def mostrar(self, target_currency, conversion_rates):
        if target_currency not in conversion_rates:
            raise ValueError(f"No hay tasas de conversión para {target_currency}.")

        total = 0
        for symbol, amount in self.balances.items():
            if symbol not in conversion_rates:
                raise ValueError(f"No se puede convertir {symbol}.")
            if target_currency not in conversion_rates[symbol]:
                raise ValueError(f"No se puede convertir {symbol} a {target_currency}.")
            # Aplicar correctamente la tasa de conversión
            total += amount / conversion_rates[symbol][target_currency]

        # Si se trata de YEN: Redondear el total al entero más cercano
        if target_currency == "YEN":
            return f"{round(total)} {target_currency}"

        # En caso contrario (EUR): No se redondea
        else:
            return f"{total:.2f} {target_currency}"