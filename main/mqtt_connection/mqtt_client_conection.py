import paho.mqtt.client as mqtt

class MqttClientConnection:
    def __init__(self, broker_ip: str, port: int, client_name:str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive

    def start_connection(self):
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, self.__client_name)
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
        self.__mqtt_client = mqtt_client
        return mqtt_client

    def end_connection(self):
        try:
            self.__mqtt_client.loop_stop
            self.__mqtt_client.disconnect()
            return True
        except:
            return False