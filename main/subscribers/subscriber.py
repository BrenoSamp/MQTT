from main.configs.broker_configs import mqtt_broker_configs
from main.mqtt_connection.callbacks import *
from main.mqtt_connection.mqtt_client_conection import MqttClientConnection
import paho.mqtt.client as mqtt

class Subscriber:
    def __init__(self):
        self.__mqtt_connection = MqttClientConnection(
            mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], 'subscriber', mqtt_broker_configs["KEEPALIVE"])
        self.__mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

    ## ALL METHODS
    def subscribeOnAllTopic(self):
        self.__mqtt_client.on_connect = on_connect_all
        self.__mqtt_client.on_message = on_message_all
        self.__mqtt_client.on_subscribe = on_subscribe_all
        self.__mqtt_connection.start_connection(self.__mqtt_client)
        self.__mqtt_client.loop_forever()