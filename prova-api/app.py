from flask import Flask, json, request
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

receitas = [
    {
        "titulo": "Lasanha",
        "ingredientes": ["Macarrão", "Queijo"],
        "modoPreparo": "Para fazer a lasanha você prmeiro...",
        "rendimento": "O rendiemnto foi de..."
    },
    {
        "titulo": "Bolo",
        "ingredientes": ["Trigo", "Ovo", "Açucar", "leite"],
        "modoPreparo": "Para fazer o bolo você prmeiro...",
        "rendimento": "O rendiemnto foi de..."
    }
]

class Receitas(Resource):
    def get(self):
        return {'status': 200, 'data': receitas};

    def post(self):
        novaReceita = json.loads(request.data);
        receitas.append(novaReceita);
        return {
            "mensagem": "Created!",
            "novaReceita": novaReceita
        }


class Receita(Resource):
    def get(self, indice):
        try:
            return receitas[indice]
        except IndexError:
            mensagem = "A receita com indice {} não foi encontrada".format(indice)
            return {
                "status": "Erro no índice",
                "mensagem": mensagem
            }  
        except:
            mensagem = "Erro desconhecido"
            return {
                "mensagem": mensagem
            } 

    def put(self, indice):
        
        novoValor = json.loads(request.data)

        receitas[indice] = novoValor

        return {
            "mensagem": "Updated",
            "novoValor": novoValor
        }

    def delete(self, indice):
        try:
            receitas.pop(indice)
            return {
                "mensagem": "deleted"
            } 
        except IndexError:  
            mensagem = "Não foi encontrado receita com o indice {}".format(indice)
            return {
                "mensagem": mensagem
            }    

api.add_resource(Receitas, "/receitas")
api.add_resource(Receita, "/receita/<int:indice>")

if __name__ == '__main__':
    app.run(debug=True)
