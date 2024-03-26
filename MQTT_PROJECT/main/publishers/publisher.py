from main.configs.broker_configs import mqtt_broker_configs
from main.mqtt_connection.callbacks import on_connect_text_editor_response, on_message_text_editor_response, on_subscribe_text_editor_response
from mqtt_connection.mqtt_client_conection import MqttClientConnection
import time

class Publisher:
    def sendToTextEditorTopic(message: str):
        mqtt_client = MqttClientConnection(
            mqtt_broker_configs["HOST"], mqtt_broker_configs["PORT"], 'text_editor_publisher', mqtt_broker_configs["KEEPALIVE"])

        mqtt_client.on_connect = on_connect_text_editor_response
        mqtt_client.on_message = on_message_text_editor_response
        mqtt_client.on_subscribe = on_subscribe_text_editor_response
        mqtt_client.connect(host=mqtt_broker_configs["HOST"], port=mqtt_broker_configs["PORT"])
        mqtt_client.publish(topic=mqtt_broker_configs['TEXT_EDITOR_TOPIC'], payload=message)
        mqtt_client.loop()

        while True: time.sleep(0.001)

    def sendToTextEditorResponseTopic(message: str, mqtt_client):
        mqtt_client.publish(topic=mqtt_broker_configs['TEXT_EDITOR_RESPONSE_TOPIC'], payload=message)