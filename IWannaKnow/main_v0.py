import tweepy as tw 
from time import sleep
import configparser
from telethon import TelegramClient
from datetime import datetime, timedelta

config = configparser.ConfigParser()
config.read('./credenciais.ini')
config.sections()

api_id = '19714192'
api_hash = 'e8d5c0892f07a2509d0a1acbea79465d'
token = 'bot token'
phone = '+5521969903976'


api_key = 'aysywmPajo3bv5ZWxtE24WiFO'
api_secret_key = '6pFf51Zu9CNe2AjcCmZDjZZo7qSqh0ow9mDyrd5AivfZXvN7lN'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAF%2FkbgEAAAAAuR1%2BB1D0s%2BxyrWfr73daYqWOwac%3DfhU7QWYYcSVXCQrmUozKBb6xboQKI4n6BLpfnJG1LGt4anobpw'
access_token = '1439283988473032710-FsV8cJeAOr6ybg1KaMctXodK860X5L'
access_secret_token = 'QdjWPwbnyWoIGoZF458UCZM76FWpDN14xXUTAwmdMD8iv'

print('startando...')
sleep(11)
#cliente = tw.Client(bearer_token=config['TWITTER']['bearer_token'], consumer_key=config['TWITTER']['api_key'], consumer_secret=config['TWITTER']['api_secret_key'], access_token=config['TWITTER']['acess_token'], access_token_secret=config['TWITTER']['acess_secret_token'])
cliente = tw.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret_key, access_token=access_token, access_token_secret=access_secret_token)
end_time = datetime.now() - timedelta(hours=3)
start_time = datetime.now() - timedelta(hours=4)
#.strftime('%d/%m/%Y %H:%M')


resposta1 = cliente.search_recent_tweets(query='tiro shopping nova américa -is:retweet lang:pt -is:quote -is:reply',start_time=start_time,end_time=end_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta2 = cliente.search_recent_tweets(query='tiroteiro shopping nova américa -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta3 = cliente.search_recent_tweets(query='assalto shopping nova américa -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta4 = cliente.search_recent_tweets(query='assaltante shopping nova américa -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta5 = cliente.search_recent_tweets(query='arrastão shopping nova américa -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data

resposta6 = cliente.search_recent_tweets(query='tiro madureira -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta7 = cliente.search_recent_tweets(query='tiroteio madureira -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta8 = cliente.search_recent_tweets(query='assalto madureira -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta9 = cliente.search_recent_tweets(query='assaltante madureira -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta10 = cliente.search_recent_tweets(query='arrastão madureira -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data
resposta11 = cliente.search_recent_tweets(query='madureira -is:retweet lang:pt -is:quote -is:reply',end_time=end_time,start_time=start_time,max_results=10,user_auth=True,tweet_fields=['context_annotations', 'created_at', 'author_id'], place_fields=['full_name']).data

dados = []

dados.append(resposta1)
dados.append(resposta2)
dados.append(resposta3)
dados.append(resposta4)
dados.append(resposta5)
dados.append(resposta6)
dados.append(resposta7)
dados.append(resposta8)
dados.append(resposta9)
dados.append(resposta10)
dados.append(resposta11)

client = TelegramClient('Gabriel', api_id, api_hash)
async def main(tt):
    await client.send_message('me', tt)


nome = ''
nome_arquivo = 'tweets.txt'
for dado in dados:
    if dado == None:
        continue
    for tt in dado:
        hora_atual = datetime.now().strftime('%Y-%m-%d %H')
        data_tt = str(tt.created_at)[:13]
        if data_tt == hora_atual:
            print('-'*50)
            print(tt.created_at)
            print(tt.author_id)
            print(tt)
            arquivo = open(nome_arquivo, '+a')
            arquivo.write(f'{str(tt)}\n')
            arquivo.close()
            try:
                print('>>>>  enviando mensagem... <<<')
                sleep(10)
    
                with client:
                    client.loop.run_until_complete(main(data_tt))
                    client.loop.run_until_complete(main(tt.text))
                print('>>>> mensagem enviada ! <<<<<')

            except Exception as e:
                print(e)
        
print('processo encerrado !')