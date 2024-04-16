from main.configs.broker_configs import mqtt_broker_configs
from main.mqtt_connection.callbacks import on_connect_text_editor, on_message_text_editor, on_subscribe_text_editor, on_connect_file_editor, on_message_file_editor, on_subscribe_file_editor, on_connect_calculate, on_message_calculate, on_subscribe_calculate
from main.mqtt_connection.mqtt_client_conection import MqttClientConnection
import paho.mqtt.client as mqtt

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

        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'text_editor_subscriber')

        mqtt_client.on_connect = on_connect_text_editor
        mqtt_client.on_message = on_message_text_editor
        mqtt_client.on_subscribe = on_subscribe_text_editor
        mqtt_client_connection.start_connection(mqtt_client)
        mqtt_client.subscribe(topic=mqtt_broker_configs['TEXT_EDITOR_TOPIC'])

        mqtt_client.loop_forever()

    ## FILE EDITOR METHODS
    @staticmethod
    def subscribeOnFileEditTopic():
        mqtt_client_connection = MqttClientConnection(
            mqtt_broker_configs["HOST"],
            mqtt_broker_configs["PORT"],
            "file_editor_subscriber",
            mqtt_broker_configs["KEEPALIVE"],
            )
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'file_editor_subscriber')
        mqtt_client.on_connect = on_connect_file_editor
        mqtt_client.on_message = on_message_file_editor
        mqtt_client.on_subscribe = on_subscribe_file_editor
        mqtt_client_connection.start_connection(mqtt_client)
        mqtt_client.subscribe(topic=mqtt_broker_configs['FILE_EDITOR_TOPIC'])

        mqtt_client.loop_forever()

    ## CALCULATE METHODS
    @staticmethod
    def subscribeOnCalculateTopic():
        mqtt_client_connection = MqttClientConnection(
            mqtt_broker_configs["HOST"],
            mqtt_broker_configs["PORT"],
            "calculate_editor_subscriber",
            mqtt_broker_configs["KEEPALIVE"],
            )
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'file_editor_subscriber')
        mqtt_client.on_connect = on_connect_calculate
        mqtt_client.on_message = on_message_calculate
        mqtt_client.on_subscribe = on_subscribe_calculate
        mqtt_client_connection.start_connection(mqtt_client)
        mqtt_client.subscribe(topic=mqtt_broker_configs['CALCULATE_TOPIC'])

        mqtt_client.loop_forever()