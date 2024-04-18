from main.configs.broker_configs import mqtt_broker_configs
from main.mqtt_connection.callbacks import *
from main.mqtt_connection.mqtt_client_conection import MqttClientConnection
import paho.mqtt.client as mqtt
import json

class Publisher:
    def __init__(self):
        self.__mqtt_connection = MqttClientConnection(
            mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], 'publisher', mqtt_broker_configs["KEEPALIVE"])
        self.__mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        self.__mqtt_client.on_connect = on_connect_all_response
        self.__mqtt_client.on_message = on_message_all_response
        self.__mqtt_connection.start_connection(self.__mqtt_client)
        self.__mqtt_client.loop_start()

    ## TEXT EDITOR METHODS
    def sendToTextEditorTopic(self, message: str):
        self.__mqtt_client.subscribe(mqtt_broker_configs['TEXT_EDITOR_RESPONSE_TOPIC'])
        self.__mqtt_client.publish(topic=mqtt_broker_configs['TEXT_EDITOR_TOPIC'], payload=message, qos=2)

    ## FILE EDITOR METHODS
    def sendToFileEditorTopic(self, message: str):
        self.__mqtt_client.subscribe(mqtt_broker_configs['FILE_EDITOR_RESPONSE_TOPIC'])
        self.__mqtt_client.publish(topic=mqtt_broker_configs['FILE_EDITOR_TOPIC'], payload=message, qos=2)

    ## CALCULATE METHODS
    def sendToCalculateTopic(self, message: dict):
        self.__mqtt_client.subscribe(mqtt_broker_configs['CALCULATE_RESPONSE_TOPIC'])
        self.__mqtt_client.publish(topic=mqtt_broker_configs['CALCULATE_TOPIC'], payload=json.dumps(message), qos=2)

    ## STOP METHODS
    def stop(self):
        self.__mqtt_client.loop_stop()
        self.__mqtt_client.disconnect()
