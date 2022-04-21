import tweepy as tw 
from time import sleep
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from datetime import datetime

api_id = '19714192'
api_hash = 'e8d5c0892f07a2509d0a1acbea79465d'
token = 'bot token'
phone = '+5521969903977'


api_key = 'aysywmPajo3bv5ZWxtE24WiFO'
api_secret_key = '6pFf51Zu9CNe2AjcCmZDjZZo7qSqh0ow9mDyrd5AivfZXvN7lN'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAF%2FkbgEAAAAAuR1%2BB1D0s%2BxyrWfr73daYqWOwac%3DfhU7QWYYcSVXCQrmUozKBb6xboQKI4n6BLpfnJG1LGt4anobpw'
access_token = '1439283988473032710-FsV8cJeAOr6ybg1KaMctXodK860X5L'
access_secret_token = 'QdjWPwbnyWoIGoZF458UCZM76FWpDN14xXUTAwmdMD8iv'

cliente = tw.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret_key, access_token=access_token, access_token_secret=access_secret_token)

start_time = datetime.now()


resposta1 = cliente.search_recent_tweets(query='madureira',end_time=start_time,max_results=10,user_auth=True)
resposta2 = cliente.search_recent_tweets(query='tiro',end_time=start_time,max_results=10,user_auth=True)
resposta3 = cliente.search_recent_tweets(query='tiroteio',end_time=start_time,max_results=10,user_auth=True)
resposta4 = cliente.search_recent_tweets(query='assalto',end_time=start_time,max_results=10,user_auth=True)
resposta5 = cliente.search_recent_tweets(query='assaltante',end_time=start_time,max_results=10,user_auth=True)

dados = []
dados1 = resposta1.data
dados2 = resposta2.data
dados3 = resposta3.data
dados4 = resposta4.data
dados5 = resposta5.data
dados.append(dados1)
dados.append(dados2)
dados.append(dados3)
dados.append(dados4)
dados.append(dados5)

for dado in dados:
    for tt in dado:
        str(tt)
        print('\n')
        print(tt)
        print('-'*50)
        with TelegramClient('session', api_id, api_hash) as client:
            if not client.is_user_authorized():
                 client.send_code_request(phone)
                 client.sign_in(phone, input('code: ')) 
            try:
                print(">>>>  enviando mensagem... <<<\n")
                sleep(10)
                receiver = InputPeerUser('user_id', 'user_hash')
                client.send_message(receiver, tt)
                print(">>>   mensagem enviada   <<<")
            except Exception as e:
                print(e);
            client.run_until_disconnected()
