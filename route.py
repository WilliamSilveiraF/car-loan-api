from flask import Flask, request
#from main import insertUsuario
from src import getRates, payment
from math import floor

from main import teste,insertUsuario,calculo

app = Flask("cars")
ipca=0

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    body = request.get_json()
    
    if("nome" not in body):
        return geraResponse(400, "O parametro nome é obrigatorio")
    if("email" not in body):
        return geraResponse(400, "O parametro email é obrigatorio")
    if("senha" not in body):
        return geraResponse(400, "O parametro senha é obrigatorio")

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])
    return geraResponse(200, "Usuario criado", "user" ,usuario)


@app.route('/api/teste', methods=["POST"])
def testando():
    body = request.get_json()
    
    test = teste(body["carprice"], body["downpayment"],body["tradeinvalue"],body["lengthofloan"],body["rate"])

    return geraResponse(200, "parcela calculada",'parcela', test)



@app.route('/api/calcaculateloan', methods=["POST"])

def pagamento():
    body = request.get_json()

    if("carprice" not in body):
        return geraResponse(400, "O parametro carprice é obrigatorio")
    if("downpayment" not in body and "tradeinvalue" not in body):
        return geraResponse(400, "O parametro de trade é obrigatorio")
    if("lengthofloan" not in body):
        return geraResponse(400, "O parametro lengthofloan é obrigatorio")
    if("rate" not in body):
        return geraResponse(400, "O parametro rate é obrigatorio")

    getRates.IPCA()
    nper = body['lengthofloan']
    dp = body['downpayment']
    ti = body['tradeinvalue']
    fv = body['carprice']
    rate = getRates.getRates(body['rate'],ipca)
    dados = payment.Payment(rate, nper,  dp, ti, fv)
    parcela= floor(dados[0],2)
    totalInterestPaid=dados[1]
    totalLoanInterestPaid=dados[2]
    Resposta = calculo(fv, dp, ti,totalInterestPaid,totalLoanInterestPaid, parcela)   
    return geraResponse(200, "parcela calculada",'Resposta', Resposta)


def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem
    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    return response

app.run()