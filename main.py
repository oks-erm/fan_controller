from machine import Pin
import dht
import network
import time
import config
from umqtt.simple import MQTTClient

# Sensor
sensor = dht.DHT22(Pin(14))

# Fan 
fan = Pin(12, Pin.OUT)
fan_state = False

TEMP_ON_THRESHOLD = 25
TEMP_OFF_THRESHOLD = 21

# Network 
SSID = config.SSID
PASSWORD = config.PASSWORD
MQTT_BROKER = config.MQTT_BROKER
TOPIC = config.TOPIC


def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass

    print('Connected to Wi-Fi')


def connect_to_mqtt(broker):
    client = MQTTClient('device_id', broker)
    client.connect()
    return client


# Connect to Wi-Fi and MQTT
connect_to_wifi(SSID, PASSWORD)
mqtt_client = connect_to_mqtt(MQTT_BROKER)


def control_fan(temp):
    global fan_state
    if not fan_state and temp > TEMP_ON_THRESHOLD:
        fan.on()
        fan_state = True
    elif fan_state and temp < TEMP_OFF_THRESHOLD:
        fan.off()
        fan_state = False


def log_temperature(temp):
    with open('temperature_log.txt', 'a') as f:
        f.write('{}: {}\n'.format(time.time(), temp))


while True:
    try:
        sensor.measure()
        temp = sensor.temperature()

        control_fan(temp)
        log_temperature(temp)
        mqtt_client.publish(TOPIC, str(temp))

        time.sleep(2)

    except OSError as e:
        print('Failed to read sensor.')
