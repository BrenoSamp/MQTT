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

    ## REQUEST FILE METHODS
    def sendToRequestFileTopic(self, message: str):
        #print("Estou me inscrevendo no " + mqtt_broker_configs['REQUEST_FILE_RESPONSE_TOPIC'] + message)
        self.__mqtt_client.subscribe(mqtt_broker_configs['REQUEST_FILE_RESPONSE_TOPIC'] + message)
        #print("Estou publicando no " + mqtt_broker_configs['REQUEST_FILE_TOPIC'] + message)
        self.__mqtt_client.publish(topic=mqtt_broker_configs['REQUEST_FILE_TOPIC'] + message, payload=message, qos=2)

    ## CALCULATE METHODS
    def sendToUploadFileTopic(self, message: str):
        #print("Estou me inscrevendo no " + mqtt_broker_configs['REQUEST_FILE_TOPIC'] + message)
        self.__mqtt_client.subscribe(mqtt_broker_configs['REQUEST_FILE_TOPIC'] + message)

    ## STOP METHODS
    def stop(self):
        self.__mqtt_client.loop_stop()
        self.__mqtt_client.disconnect()
