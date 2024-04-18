from main.configs.broker_configs import mqtt_broker_configs
import json

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

    elif topico == mqtt_broker_configs["FILE_EDITOR_TOPIC"]:
        message_payload = message.payload.decode('utf-8')
        with open('main/data/file.txt', 'a') as file:
            file.write(message_payload + '\n')
        message = 'O texto `' + message_payload + '` foi adicionado ao arquivo\n'
        client.publish(topic=mqtt_broker_configs['FILE_EDITOR_RESPONSE_TOPIC'], payload=message, qos=2)
        client.loop_stop()

    elif topico == mqtt_broker_configs["TEXT_EDITOR_TOPIC"]:
        message_payload = message.payload.decode('utf-8')
        message = 'Olá ' + message_payload + ', recebemos sua mensagem\n'
        client.publish(topic=mqtt_broker_configs['TEXT_EDITOR_RESPONSE_TOPIC'], payload=message, qos=0)
        client.loop_stop()

# Funções callbacks para tópicos de resposta
def on_connect_all_response(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_message_all_response(client, userdata, message):
    topico = message.topic
    print(f'Cliente se inscreveu no tópico: {topico}!\n')
    message_payload = message.payload.decode('utf-8')
    print(message_payload)
    client.unsubscribe(topico)
