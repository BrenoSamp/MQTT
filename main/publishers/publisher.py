from main.configs.broker_configs import mqtt_broker_configs
from main.mqtt_connection.callbacks import on_connect_text_editor_response, on_message_text_editor_response, on_subscribe_text_editor_response, on_connect_file_editor_response, on_message_file_editor_response, on_subscribe_file_editor_response, on_connect_calculate_response, on_message_calculate_response, on_subscribe_calculate_response
from main.mqtt_connection.mqtt_client_conection import MqttClientConnection
import paho.mqtt.client as mqtt

class Publisher:
    ## TEXT EDITOR METHODS
    def sendToTextEditorTopic(message: str):
        mqttConection = MqttClientConnection(
        mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], 'text_editor_publisher', mqtt_broker_configs["KEEPALIVE"])
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'text_editor_publisher')
        mqtt_client.on_connect = on_connect_text_editor_response
        mqtt_client.on_message = on_message_text_editor_response
        mqtt_client.on_subscribe = on_subscribe_text_editor_response

        mqttConection.start_connection(mqtt_client)
        mqtt_client.subscribe(mqtt_broker_configs['TEXT_EDITOR_RESPONSE_TOPIC'])
        mqtt_client.publish(topic=mqtt_broker_configs['TEXT_EDITOR_TOPIC'], payload=message)
        mqtt_client.loop_start()

    ## FILE EDITOR METHODS
    def sendToFileEditorTopic(message: str):
        mqttConnection = MqttClientConnection(
        mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], 'file_editor_publisher', mqtt_broker_configs["KEEPALIVE"])
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'file_editor_publisher')

        mqtt_client.on_connect = on_connect_file_editor_response
        mqtt_client.on_message = on_message_file_editor_response
        mqtt_client.on_subscribe = on_subscribe_file_editor_response
        mqttConnection.start_connection(mqtt_client)
        mqtt_client.subscribe(mqtt_broker_configs['FILE_EDITOR_RESPONSE_TOPIC'])
        mqtt_client.publish(topic=mqtt_broker_configs['FILE_EDITOR_TOPIC'], payload=message)
        mqtt_client.loop_start()

    ## CALCULATE METHODS
    def sendToCalculateTopic(message: str):
        mqttConnection = MqttClientConnection(
            mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], 'calculate_publisher', mqtt_broker_configs["KEEPALIVE"])
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'calculate_publisher')
        mqtt_client.on_connect = on_connect_calculate_response
        mqtt_client.on_message = on_message_calculate_response
        mqtt_client.on_subscribe = on_subscribe_calculate_response
        mqttConnection.start_connection(mqtt_client)
        mqtt_client.subscribe(mqtt_broker_configs['CALCULATE_RESPONSE_TOPIC'])
        mqtt_client.publish(topic=mqtt_broker_configs['CALCULATE_TOPIC'], payload=message)
        mqtt_client.loop_start()