import unittest
from io import StringIO
import sys
# Importar la función calculadora
from main import calculadora


def simulate_input(inputs):
    return StringIO("\n".join(map(str, inputs)) + "\n")


class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        sys.stdin = simulate_input([1, 3, 5, 10, 15])
        sys.stdout = StringIO()
        calculadora()
        output = sys.stdout.getvalue().strip()
        self.assertIn("Resultado de la suma: 30.0", output)

    def test_resta(self):
        sys.stdin = simulate_input([2, 3, 20, 5, 3])
        sys.stdout = StringIO()
        calculadora()
        output = sys.stdout.getvalue().strip()
        self.assertIn("Resultado de la resta: 12.0", output)

    def test_multiplicacion(self):
        sys.stdin = simulate_input([3, 2, 4, 5])
        sys.stdout = StringIO()
        calculadora()
        output = sys.stdout.getvalue().strip()
        self.assertIn("Resultado de la multiplicación: 20.0", output)

    def test_division(self):
        sys.stdin = simulate_input([4, 2, 20, 4])
        sys.stdout = StringIO()
        calculadora()
        output = sys.stdout.getvalue().strip()
        self.assertIn("Resultado de la división: 5.0", output)

    def test_division_por_cero(self):
        sys.stdin = simulate_input([4, 2, 10, 0])
        sys.stdout = StringIO()
        calculadora()
        output = sys.stdout.getvalue().strip()
        self.assertIn("Error: División por cero no permitida.", output)


if __name__ == "__main__":
    unittest.main()
