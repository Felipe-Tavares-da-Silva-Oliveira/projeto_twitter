import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

#Cadastrar as chaves de acesso
consumer_key = "SjpxhjTo0f9a9uNAfzGrORuQO"
consumer_secret = "oh8c8O8h3XAt5khmQWNcUQE3870fQfrmQGYk7vJML0jbXX0wdE"

access_token = "910638257385431040-SAGmZcDbs0VTclcrx7Ud1fa3l0TzKPD"
access_token_secret = "IT1ftNXPwz1przZNQo88sB8BtWYcbUOT5V7sV8K0sPpbq"

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
