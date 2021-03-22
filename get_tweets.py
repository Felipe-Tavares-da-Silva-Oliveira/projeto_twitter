import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

#Cadastrar as chaves de acesso
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"

access_token = "access_token"
access_token_secret = "access_token_secret"

# Definir um arquivo de saída para armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets_{data_hoje}.txt","w")

# Implementar uma classe para conexão com o Twitter
#aqui estamos plicando uma erança a classe MyListener esta alterando 2 metodos da classe StreamListener
class MyListener(StreamListener):
    
    def on_data(self, data):
        #realizando parsse do arquivo
        itemString = json.dumps(data)
        #escrevendo dado no arquivo
        out.write(itemString + "\n")
        return True
    
    def on_error(self, status):
        print(status)

# Implementar a função MAIN
#aqui inicia a execução do nosso código
if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    
    stream = Stream(auth, l)
    #abrindo conexão com titter - texto ou palavra que vamos monitorar
    stream.filter(track=["Trump"])
