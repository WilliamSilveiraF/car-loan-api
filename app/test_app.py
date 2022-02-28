import unittest
from src import payment

class TestPayment(unittest.TestCase):
    def test_payment(self):
        monthlyPayment =  payment.payment(0.08, 10, -10000, 0, 1)
        monthlyPayment = round(monthlyPayment, 2)
        self.assertEqual(monthlyPayment, 1030.16, "\n\napp.src.payment - Error: monthly payment must be equal 1030.16")

    def test_payment2(self):
        monthlyPayment = payment.payment(0.06, 216, 0, -50000, 0)
        monthlyPayment = round(monthlyPayment, 2)
        self.assertEqual(monthlyPayment, 129.08,"\n\napp.src.payment - Error: monthly payment must be equal 129.08")