import paho.mqtt_client as mqtt
from main.configs.broker_configs import mqtt_broker_configs

mqtt_client = mqtt.Client('publisher')
mqtt_client.connect(host=mqtt_broker_configs["HOST"], port=mqtt_broker_configs["PORT"])
mqtt_client.publish(topic='', payload='{}')