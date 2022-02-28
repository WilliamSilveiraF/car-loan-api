import unittest

import requests
from src import payment

class TestPayment(unittest.TestCase):
    def test_payment(self):
        monthlyPayment =  payment.payment(0.08, 10, -10000, 0, 1)
        monthlyPayment = round(monthlyPayment, 2)
        self.assertEqual(monthlyPayment, 1030.16, "\n\napp.src.payment - Error: monthly payment must be equal 1030.16")

    def test_payment2(self):
        monthlyPayment = payment.payment(0.06, 216, 0, -50000, 0)
        monthlyPayment = round(monthlyPayment, 2)
        self.assertEqual(monthlyPayment, 129.08,"\n\napp.src.payment.payment - Error: monthly payment must be equal 129.08")

    def test_api_calculate_loan(self):
        payload = {
            "carprice": 50000,
            "downpayment": 0,
            "tradeinvalue": 0,
            "lengthofloan": 18,
            "rate": 0.06
        }
        response = requests.post('https://car-loan-api.herokuapp.com/api/calcaculateloan', json=payload)
        
        print(f"Calling https://car-loan-api.herokuapp.com/api/calcaculateloan")
        print(f"Status code: {response.status_code}")

        self.assertEqual(
            response.status_code, 
            200, 
            f"app.main.calculateloan - Error: calculateloan fail with {response.status_code}"
        )
        
        body = response.json()

        self.assertEqual(
            body["carprice"], 
            payload["carprice"], 
            f"app.main.calculateloan - Error: carprice payloand and response body can't be diferents"
        )

        self.assertEqual(
            body["monthlyPayment"],
            2897.1,
            f"app.main.calculateloan - Error: monthly payment must be equal 2897.1 for {payload}"
        )
        
        self.assertEqual(
            body["totalInterestPaid"],
            2147.8,
            f"app.main.calculateloan - Error: total interest paid must be equal 2147.8 for {payload}"
        )

        self.assertEqual(
            body["totalLoanAndInterestPaid"],
            52147.8,
            f"app.main.calculateloan - Error: the sum total loan and interest paid must be equal 52147.8 for {payload}"
        )