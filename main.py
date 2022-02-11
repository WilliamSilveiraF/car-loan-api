
def teste(carprice, downpayment, tradeinvalue,lengthofloan,rate):
    return {"carprice": carprice, "downpayment": downpayment,"tradeinvalue": tradeinvalue,"lengthofloan": lengthofloan,"rate": rate}

def insertUsuario(nome, email, senha):
    return {"id": 1, "nome": nome}


def calculo(carprice, downpayment, tradeinvalue,totalInterestPaid,totalLoanInterestPaid, monthlyPayment):
    return {"carprice": carprice, "downpayment": downpayment,"tradeinvalue": tradeinvalue,"totalInterestPaid": totalInterestPaid,"totalLoanInterestPaid": totalLoanInterestPaid,"monthlyPayment": monthlyPayment}