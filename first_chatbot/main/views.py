
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests
import json

psid = "g.a000gAhXVetZUxHx_R03kb2QwAHjNXQ7qnn0KPzVBIx7lkwNL3AS9ogse_KDLLYy3_TV1akL2AACgYKAXcSAQASFQHGX2MiBBVwDfLP9MHphNjqY7tSERoVAUF8yKqd5OFEU2aew44nhD8DY1XP0076"
psidts = "sidts-CjIBPVxjSp_yC6eh6m-31i6Oc_VMJSqkXPBA6RW5xCvosjNCKiHmCKvlkGIFMF915IcdrRAA"
psidcc = "ABTWhQGn4gqIRWf9pi0yrn3WQNLbv1kAAooKfPjWQ16bUKTcaIqMLo-ZKdgDZHpxqjp6HbOl"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}
#cria o objeto bard para ser usado
#bard = BardCookies(cookie_dict=tokenCookies)

mockedResponse = '{"content": "bla bla bla bla bla bla bla bla", "conversetionId": "129382193721bjd"}'
enableMock = True

#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        bard =  None
        answer = json.loads(mockedResponse)    
            
        if enableMock == False:
             bard = BardCookies(cookie_dict=tokenCookies)
        #pega os dados que veio na requisição
        data = request.data

        #pega o dados da conversationId caso ele seja informado para mander a mesma conversa com o chatbot
        conversationId = data.get("conversationId")

        #verifica se o id da conversa foi recebido
        if(conversationId is not None):

            #informa o bard para responder na conversa desejada
            bard.conversation_id = conversationId
        elif enableMock == False:
            bard.conversation_id = None
        
        #answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

