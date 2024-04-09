from main.configs.broker_configs import mqtt_broker_configs

# Funções callbacks para tópico de edição de texto
def on_connect_text_editor(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['TEXT_EDITOR_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_text_editor(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["TEXT_EDITOR_TOPIC"]}\n')
    print(f'QOS: {granted_qos}')

def on_message_text_editor(client, userdata, message):
    print('Mensagem recebida!\n')
    print(f'{client}\n')
    message = f'Olá {message.payload}, recebemos sua mensagem\n'
    client.publish(topic=mqtt_broker_configs['TEXT_EDITOR_RESPONSE_TOPIC'], payload=message)

# Funções callbacks para tópico de resposta de edição de texto
def on_connect_text_editor_response(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['TEXT_EDITOR_RESPONSE_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_text_editor_response(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["TEXT_EDITOR_RESPONSE_TOPIC"]}\n')
    print(f'QOS: {granted_qos}')

def on_message_text_editor_response(client, userdata, message):
    print('Mensagem recebida!\n')
    print(f'{client}\n')
    print(f'{message.payload}')
    client.loopstop()

# Funções callbacks para tópico de edição de arquivo
def on_connect_file_editor(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['FILE_EDITOR_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_file_editor(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["FILE_EDITOR_TOPIC"]}\n')
    print(f'QOS: {granted_qos}')

def on_message_file_editor(client, userdata, message):
    print('Mensagem recebida!\n')
    print(f'{client}\n')
    file = open('main/data/file.txt')
    file.writelines(f'{message.payload}')
    message = f'O texto `{message.payload}` foi adicionado ao arquivo\n'
    client.publish(topic=mqtt_broker_configs['FILE_EDITOR_RESPONSE_TOPIC'], payload=message)

# Funções callbacks para tópico de resposta de edição de arquivo
def on_connect_file_editor_response(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['FILE_EDITOR_RESPONSE_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_file_editor_response(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["FILE_EDITOR_RESPONSE_TOPIC"]}\n')
    print(f'QOS: {granted_qos}')

def on_message_file_editor_response(client, userdata, message):
    print('Mensagem recebida!\n')
    print(f'{client}\n')
    print(f'{message.payload}')
    client.loopstop()

# Funções callbacks para tópico de cálculo
def on_connect_calculate(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['FILE_EDITOR_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_calculate(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["FILE_EDITOR_TOPIC"]}\n')
    print(f'QOS: {granted_qos}')

def on_message_calculate(client, userdata, message):
    print('Mensagem recebida!\n')
    print(f'{client}\n')
    firstValue = message.payload['first_value']
    secondValue = message.payload['second_value']
    soma = firstValue + secondValue
    subtracao = firstValue - secondValue
    divisao = firstValue / secondValue
    multiplicacao = firstValue * secondValue
    message = f'Soma: {soma}\n Subtração: {subtracao}\n Divisão: {divisao}\n Multiplicação: {multiplicacao}'
    client.publish(topic=mqtt_broker_configs['CALCULATE_RESPONSE_TOPIC'], payload=message)

# Funções callbacks para tópico de resposta de calculo
def on_connect_calculate_response(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente conectado com Sucesso')
        client.subscribe(mqtt_broker_configs['CALCULATE_RESPONSE_TOPIC'])
    else:
        print(f'Erro ao me conectar, codigo: {rc}')

def on_subscribe_calculate_response(client, userdata, mid, granted_qos):
    print(f'Cliente se inscreveu no tópico: {mqtt_broker_configs["CALCULATE_RESPONSE_TOPIC"]}\n')
    print(f'QOS: {granted_qos}')

def on_message_calculate_response(client, userdata, message):
    print('Mensagem recebida!\n')
    print(f'{client}\n')
    print(f'{message.payload}')
    client.loopstop()