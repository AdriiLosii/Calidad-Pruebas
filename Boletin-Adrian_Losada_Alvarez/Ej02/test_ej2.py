import unittest
from ej2 import Currency, Wallet

class Euro(Currency):
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("La cantidad inicial no puede ser negativa.")
        self.symbol, self.amount = "EUR", amount

class Yen(Currency):
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("La cantidad inicial no puede ser negativa.")
        if type(amount) != int:
            raise ValueError("El valor de los Yenes inicial debe ser un entero")
        self.symbol, self.amount = "YEN", amount

class TestCurrencyAndWallet(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.money_price = {
            "EUR": {"EUR": 1, "YEN": 0.007},
            "YEN": {"EUR": 142.9, "YEN": 1},
        }
        self.euro = Euro(10)
        self.yen = Yen(1000)

    # Pruebas del boletín
    def test_boletin(self):
        n = Euro(3)
        n = n.suma(3)
        n = n.multiplica(2)
        n = n.resta(2)
        self.assertEqual(n.mostrar(), "10.00 EUR")
        print(n.mostrar())

        a = Wallet()
        a.suma(n)
        a.suma(Yen(1000))
        self.assertEqual(a.mostrar("EUR", self.money_price), "17.00 EUR")
        print(a.mostrar("EUR", self.money_price))
        self.assertEqual(a.mostrar("YEN", self.money_price), "2429 YEN")
        print(a.mostrar("YEN", self.money_price))

    # Pruebas para Currency
    def test_currency_valid_operations(self):
        self.assertEqual(self.euro.suma(5.00).amount, 15.00)        # Sumar
        self.assertEqual(self.euro.resta(3.00).amount, 12.00)       # Restar
        self.assertEqual(self.euro.multiplica(2.00).amount, 24.00)  # Multiplicar
        self.assertEqual(self.euro.mostrar(), "24.00 EUR")          # Mostrar

    def test_currency_invalid_operations(self):
        # Cantidades negativas no permitidas
        with self.assertRaises(ValueError): self.euro = Euro(-10.00)
        with self.assertRaises(ValueError): self.euro = Yen(-50)
        with self.assertRaises(ValueError): self.euro.suma(-5.00)
        with self.assertRaises(ValueError): self.euro.resta(-2.50)
        with self.assertRaises(ValueError): self.euro.multiplica(-2.00)

        # Decimales en Yen no permitidos
        with self.assertRaises(ValueError): self.yen = Yen(100.50)

    # Pruebas para Wallet
    def test_wallet_operations(self):
        wallet = Wallet()
        wallet.suma(self.euro)
        wallet.suma(Yen(1000))

        # Mostrar el total en una moneda específica
        self.assertEqual(wallet.mostrar("EUR", self.money_price), "17.00 EUR")
        self.assertEqual(wallet.mostrar("YEN", self.money_price), "2429 YEN")

        # Unidad monetaria dollar USD no definida
        with self.assertRaises(ValueError): self.assertEqual(wallet.mostrar("USD", self.money_price), "17.85 USD")

    def test_wallet_negative_balance(self):
        wallet = Wallet()
        wallet.suma(Euro(5))
        wallet.resta(Euro(10))  # Permitido balance negativo
        self.assertEqual(wallet.mostrar("EUR", self.money_price), "-5.00 EUR")

    def test_wallet_conversion(self):
        wallet = Wallet()
        wallet.suma(self.euro)
        wallet.suma(self.yen)

        # Conversión a otra moneda
        total_in_euros = wallet.mostrar("EUR", self.money_price)
        total_in_yen = wallet.mostrar("YEN", self.money_price)

        self.assertEqual(total_in_euros, "17.00 EUR")
        self.assertEqual(total_in_yen, "2429 YEN")

if __name__ == "__main__":
    unittest.main()