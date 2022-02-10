from flask import Flask, request
#from main import insertUsuario
from getRates import *
from payment import payment
from math import floor

app = Flask("cars")

@app.route('/car', methods=["POST"])
def pagamento():
    body = request.get_json()
    
    if("carprice" not in body):
        return geraResponse(400, "O parametro carprice é obrigatorio")
    
    if("downpayment" or "tradeinvalue" not in body):
        return geraResponse(400, "O parametro de trade é obrigatorio")

    if("lengthofloan" not in body):
        return geraResponse(400, "O parametro lengthofloan é obrigatorio")

    if("rate" not in body):
        return geraResponse(400, "O parametro rate é obrigatorio")

    nper = body['lengthofloan']
    pv = body['downpayment']+body['tradeinvalue']
    fv = body['carprice']
    rate = getRates(body['rate'],IPCA).monthlyRealNetRate
    floor(rate,2)
    parcela = payment(rate, nper, pv, fv=0, type=1)
    return geraResponse(200, "parcela calculada",'parcela', parcela)



def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response

app.run()