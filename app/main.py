from flask import Flask, request
from .src import payment

app = Flask(__name__)

@app.route('/api/calcaculateloan', methods=["POST"])

def calcaculateloan():
    body = request.get_json()

    if("carprice" not in body):
        return generateResponse(400, "O parametro carprice é obrigatório")
    if("downpayment" not in body):
        return generateResponse(400, "O parametro downpayment é obrigatório")
    if("tradeinvalue" not in body):
        return generateResponse(400, "O parametro tradeinvalue é obrigatorio")
    if("lengthofloan" not in body):
        return generateResponse(400, "O parametro lengthofloan é obrigatorio")
    if("rate" not in body):
        return generateResponse(400, "O parametro rate é obrigatorio")

    #IPCA = getRates.IPCA
    #rate = getRates.getRates(body['rate'], IPCA).monthlyRealNetRate
    rate = body["rate"]
    nper = body['lengthofloan']
    pv = -(body['carprice'] - (body['downpayment'] + body['tradeinvalue']))
    fv = 0

    monthlyPayment =  payment.payment(rate, nper, pv, fv, 1)
    monthlyPayment = round(monthlyPayment, 2)

    totalInterestPaid = (monthlyPayment * nper) + pv
    totalInterestPaid = round(totalInterestPaid, 2)

    totalLoanAndInterestPaid = monthlyPayment * nper
    totalLoanAndInterestPaid = round(totalLoanAndInterestPaid, 2)

    response = {}
    response["status"] = 200
    response["message"] = "success"
    response["carprice"] = body["carprice"]
    response["downpayment"] = body["downpayment"]
    response["tradeinvalue"] = body["tradeinvalue"]
    response["totalInterestPaid"] = totalInterestPaid
    response["totalLoanAndInterestPaid"] = totalLoanAndInterestPaid
    response["monthlyPayment"] = monthlyPayment
    
    return response

def generateResponse(status, message, contentName=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message
    if(contentName and content):
        response[contentName] = content
    
    return response
