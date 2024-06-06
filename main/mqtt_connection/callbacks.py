from main.configs.broker_configs import mqtt_broker_configs
import json
import glob
import base64
import os

# Funções callbacks para tópicos de requisições
def on_connect_all(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['ALL_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_all(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["ALL_TOPIC"]}\n')

def on_message_all(client, userdata, message):
    topico = message.topic
    print(f'Mensagem recebida no topico {topico}!\n')
    if topico == mqtt_broker_configs["CALCULATE_TOPIC"]:
        payload = json.loads(message.payload)
        firstValue = float(payload['first_value'])
        secondValue = float(payload['second_value'])
        soma = firstValue + secondValue
        subtracao = firstValue - secondValue
        divisao = firstValue / secondValue
        multiplicacao = firstValue * secondValue
        message = "Soma: {} \nSubtração: {} \nDivisão: {} \nMultiplicação: {} \n".format(soma, subtracao, divisao, multiplicacao)
        client.publish(topic=mqtt_broker_configs['CALCULATE_RESPONSE_TOPIC'], payload=message, qos=2)
        client.loop_stop()

    elif topico == mqtt_broker_configs["REQUEST_FILE_TOPIC"]:
        message_payload = message.payload.decode('utf-8')
        message = 'Olá ' + message_payload + ', recebemos sua mensagem\n'
        client.publish(topic=mqtt_broker_configs['REQUEST_FILE_RESPONSE_TOPIC'], payload=message, qos=0)
        client.loop_stop()

# Funções callback
def on_connect_all_response(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_message_all_response(client, userdata, message):
    # Configuração do diretório base da aplicação
    # Supondo que este arquivo está em "programa/main/mqtt_connection, volta 3 pastas para pegar o dir"
    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    # Divide o tópico em partes
    topico = message.topic
    reqOuRes = topico.split('/')[0]
    tipo = topico.split('/')[1]
    nome = topico.split('/')[2]

    if reqOuRes == "request":
        # Procura o arquivo no dir+tipo, com o nome e sendo de qualquer extensão
        search_path = os.path.join(dir, tipo, nome + ".*")
        file_list = glob.glob(search_path)

        if file_list:
            # Pega o primeiro arquivo que foi encontrado
            filepath = file_list[0]
            # Codifica esse arquivo em bytes para enviar via mensagem
            with open(filepath, "rb") as file:
                encoded_file = base64.b64encode(file.read())
            # Obtém a extensão sem o ponto
            ext = os.path.splitext(filepath)[1][1:]
            # Publica o nome da extensão e o arquivo codificado no canal de response
            print(f"Estou publicando no response/{tipo}/{nome}")
            client.publish(f"response/{tipo}/{nome}", f"{ext},{encoded_file.decode('utf-8')}")
    elif reqOuRes == "response":
        # Remove a assinatura do tópico de receber arquivos codificados
        client.unsubscribe(topico)
        # Separa a mensagem recebida em extensão e conteúdo
        payload = message.payload.decode('utf-8')
        ext, encoded_file = payload.split(',', 1)
        # Escolhe o diretório para salvar
        save_path = os.path.join(dir, tipo, nome + '.' + ext)
        # Transforma e salva o arquivo com a extensão correta
        with open(save_path, "wb") as file:
            file.write(base64.b64decode(encoded_file))
        # Assina o tópico para receber requisições futuras
        print(f"Estou me inscrevendo no request/{tipo}/{nome}")
        client.subscribe(f"request/{tipo}/{nome}")