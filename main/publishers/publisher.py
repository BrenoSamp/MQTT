from main.configs.broker_configs import mqtt_broker_configs
from main.mqtt_connection.callbacks import on_connect_text_editor_response, on_message_text_editor_response, on_subscribe_text_editor_response, on_connect_file_editor_response, on_message_file_editor_response, on_subscribe_file_editor_response, on_connect_calculate_response, on_message_calculate_response, on_subscribe_calculate_response
from main.mqtt_connection.mqtt_client_conection import MqttClientConnection
import paho.mqtt.client as mqtt
import json

class Publisher:
    def __init__(self):
        self.__mqtt_connection = MqttClientConnection(
            mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], 'publisher', mqtt_broker_configs["KEEPALIVE"])
        self.__mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)


    ## TEXT EDITOR METHODS
    def sendToTextEditorTopic(self, message: str):
        self.__mqtt_client.on_connect = on_connect_text_editor_response
        self.__mqtt_client.on_message = on_message_text_editor_response
        self.__mqtt_client.on_subscribe = on_subscribe_text_editor_response

        self.__mqtt_connection.start_connection(self.__mqtt_client)
        self.__mqtt_client.subscribe(mqtt_broker_configs['TEXT_EDITOR_RESPONSE_TOPIC'])
        self.__mqtt_client.publish(topic=mqtt_broker_configs['TEXT_EDITOR_TOPIC'], payload=message, qos=2)
        self.__mqtt_client.loop_start()

    ## FILE EDITOR METHODS
    def sendToFileEditorTopic(self, message: str):
        self.__mqtt_client.on_connect = on_connect_file_editor_response
        self.__mqtt_client.on_message = on_message_file_editor_response
        self.__mqtt_client.on_subscribe = on_subscribe_file_editor_response
        self.__mqtt_connection.start_connection(self.__mqtt_client)
        self.__mqtt_client.subscribe(mqtt_broker_configs['FILE_EDITOR_RESPONSE_TOPIC'])
        self.__mqtt_client.publish(topic=mqtt_broker_configs['FILE_EDITOR_TOPIC'], payload=message, qos=2)
        self.__mqtt_client.loop_start()

    ## CALCULATE METHODS
    def sendToCalculateTopic(self, message: dict):
        self.__mqtt_client.on_connect = on_connect_calculate_response
        self.__mqtt_client.on_message = on_message_calculate_response
        self.__mqtt_client.on_subscribe = on_subscribe_calculate_response
        self.__mqtt_connection.start_connection(self.__mqtt_client)
        self.__mqtt_client.subscribe(mqtt_broker_configs['CALCULATE_RESPONSE_TOPIC'])
        self.__mqtt_client.publish(topic=mqtt_broker_configs['CALCULATE_TOPIC'], payload=json.dumps(message), qos=2)
        self.__mqtt_client.loop_start()