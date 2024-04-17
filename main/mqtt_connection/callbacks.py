from main.configs.broker_configs import mqtt_broker_configs
import json

# Funções callbacks para tópico de edição de texto
def on_connect_text_editor(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['TEXT_EDITOR_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_text_editor(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["TEXT_EDITOR_TOPIC"]}\n')

def on_message_text_editor(client, userdata, message):
    print('Mensagem recebida!\n')
    message = 'Olá' + message.payload + ', recebemos sua mensagem\n'
    client.publish(topic=mqtt_broker_configs['TEXT_EDITOR_RESPONSE_TOPIC'], payload=message, qos=2)
    client.loop_stop()

# Funções callbacks para tópico de resposta de edição de texto
def on_connect_text_editor_response(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_text_editor_response(client, userdata, mid, granted_qos):
    print('Cliente se inscreveu no tópico: ' + mqtt_broker_configs["TEXT_EDITOR_RESPONSE_TOPIC"] + '\n')

def on_message_text_editor_response(client, userdata, message):
    print(message.payload)
    client.loop_stop()

# Funções callbacks para tópico de edição de arquivo
def on_connect_file_editor(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['FILE_EDITOR_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_file_editor(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["FILE_EDITOR_TOPIC"]}\n')

def on_message_file_editor(client, userdata, message):
    print('Mensagem recebida!\n')
    file = open('main/data/file.txt', 'w')
    file.writelines(message.payload)
    file.close()
    message = 'O texto `' + message.payload + '` foi adicionado ao arquivo\n'
    client.publish(topic=mqtt_broker_configs['FILE_EDITOR_RESPONSE_TOPIC'], payload=message, qos=2)
    client.loop_stop()

# Funções callbacks para tópico de resposta de edição de arquivo
def on_connect_file_editor_response(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_file_editor_response(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["FILE_EDITOR_RESPONSE_TOPIC"]}\n')

def on_message_file_editor_response(client, userdata, message):
    print(f'{message.payload}')
    client.loop_stop()

# Funções callbacks para tópico de cálculo
def on_connect_calculate(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['CALCULATE_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_calculate(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["CALCULATE_TOPIC"]}\n')

def on_message_calculate(client, userdata, message):
    print('Mensagem recebida!\n')
    payload = json.loads(message.payload)
    firstValue = float(payload['first_value'])
    secondValue = float(payload['second_value'])
    soma = firstValue + secondValue
    subtracao = firstValue - secondValue
    divisao = firstValue / secondValue
    multiplicacao = firstValue * secondValue
    message = "Soma: {} \nSubtração: {} \nDivisão: {} \nMultiplicação".format(soma, subtracao, divisao, multiplicacao)
    client.publish(topic=mqtt_broker_configs['CALCULATE_RESPONSE_TOPIC'], payload=message, qos=2)
    client.loop_stop()

# Funções callbacks para tópico de resposta de calculo
def on_connect_calculate_response(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_calculate_response(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["CALCULATE_RESPONSE_TOPIC"]}\n')

def on_message_calculate_response(client, userdata, message):
    print('Mensagem recebida!\n')
    print(message.payload)
    client.loop_stop()