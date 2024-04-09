from main.configs.broker_configs import mqtt_broker_configs
from main.mqtt_connection.callbacks import on_connect_text_editor, on_message_text_editor, on_subscribe_text_editor, on_connect_file_editor, on_message_file_editor, on_subscribe_file_editor
from main.mqtt_connection.mqtt_client_conection import MqttClientConnection
import time

class Subscriber:

    ## TEXT EDITOR METHODS
    @staticmethod
    def subscribeOnTextEditTopic():
        mqtt_client_connection = MqttClientConnection(
            mqtt_broker_configs["HOST"],
            mqtt_broker_configs["PORT"],
            "text_editor_subscriber",
            mqtt_broker_configs["KEEPALIVE"],
            )
        mqtt_client.on_connect = on_connect_text_editor
        mqtt_client.on_message = on_message_text_editor
        mqtt_client.on_subscribe = on_subscribe_text_editor
        mqtt_client = mqtt_client_connection.start_connection()

        mqtt_client.loop()

        while True: time.sleep(0.001)

    ## FILE EDITOR METHODS
    @staticmethod
    def subscribeOnFileEditTopic():
        mqtt_client_connection = MqttClientConnection(
            mqtt_broker_configs["HOST"],
            mqtt_broker_configs["PORT"],
            "file_editor_subscriber",
            mqtt_broker_configs["KEEPALIVE"],
            )
        mqtt_client.on_connect = on_connect_text_editor
        mqtt_client.on_message = on_message_file_editor
        mqtt_client.on_subscribe = on_subscribe_file_editor
        mqtt_client = mqtt_client_connection.start_connection()

        mqtt_client.loop()

        while True: time.sleep(0.001)