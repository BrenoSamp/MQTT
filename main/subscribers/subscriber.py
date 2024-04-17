from main.configs.broker_configs import mqtt_broker_configs
from main.mqtt_connection.callbacks import on_connect_text_editor, on_message_text_editor, on_subscribe_text_editor, on_connect_file_editor, on_message_file_editor, on_subscribe_file_editor, on_connect_calculate, on_message_calculate, on_subscribe_calculate
from main.mqtt_connection.mqtt_client_conection import MqttClientConnection
import paho.mqtt.client as mqtt

class Subscriber:
    def __init__(self):
        self.__mqtt_connection = MqttClientConnection(
            mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], 'calculate_publisher', mqtt_broker_configs["KEEPALIVE"])
        self.__mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

    ## TEXT EDITOR METHODS
    def subscribeOnTextEditTopic(self):

        self.__mqtt_client.on_connect = on_connect_text_editor
        self.__mqtt_client.on_message = on_message_text_editor
        self.__mqtt_client.on_subscribe = on_subscribe_text_editor
        self.__mqtt_connection.start_connection(self.__mqtt_client)
        self.__mqtt_client.loop_forever()

    ## FILE EDITOR METHODS
    def subscribeOnFileEditTopic(self):
        self.__mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'file_editor_subscriber')
        self.__mqtt_client.on_connect = on_connect_file_editor
        self.__mqtt_client.on_message = on_message_file_editor
        self.__mqtt_client.on_subscribe = on_subscribe_file_editor
        self.__mqtt_connection.start_connection(self.__mqtt_client)
        self.__mqtt_client.loop_forever()

    ## CALCULATE METHODS
    def subscribeOnCalculateTopic(self):
        self.__mqtt_client.on_connect = on_connect_calculate
        self.__mqtt_client.on_message = on_message_calculate
        self.__mqtt_client.on_subscribe = on_subscribe_calculate
        self.__mqtt_connection.start_connection(self.__mqtt_client)
        self.__mqtt_client.loop_forever()