from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

import random, time
import adafruit_dht
import board

#board.D26 refers to GPIO 26 on the Raspberry Pi. Physical Pin Number on Raspberry Pi: Pin 37

dht_device = adafruit_dht.DHT11(board.D26)


# A random prog rammatic shadow client ID .

SHADOW_CLIENT = "myShadowClient10"

#Find host name from domain configurations use domain name
HOST_NAME = "xxxxxxxxxx"


ROOT_CA = "xxxxxxxx.crt"


PRIVATE_KEY = "xxxxxxxx.private.key"

CERT_FILE = "xxxxxxxxxxx.cert.pem"

# IoT core Thing name .

SHADOW_HANDLER = "xxxxxxx"

# Automatically called whenever the shadow is updated .

def myShadowUpdateCallback(payload, responseStatus, token):
    print()


myShadowClient = AWSIoTMQTTShadowClient( SHADOW_CLIENT)
myShadowClient.configureEndpoint (HOST_NAME, 8883)

myShadowClient.configureCredentials (ROOT_CA, PRIVATE_KEY,CERT_FILE)

myShadowClient.configureConnectDisconnectTimeout(10)

myShadowClient.configureMQTTOperationTimeout(5)

myShadowClient.connect()

# Create a prog rammatic representation of the shadow ,

myDeviceShadow = myShadowClient.createShadowHandlerWithName(SHADOW_HANDLER, True)



while True:
    start_sensor_reading = time.time()
    
    temperature_c = dht_device.temperature
    temperature_f = temperature_c * (9 / 5) + 32

    humidity = dht_device.humidity
    end_sensor_reading = time.time()
    sensor_reading_latency = end_sensor_reading - start_sensor_reading

    print(f"Sensor Reading Latency: {sensor_reading_latency:.4f} seconds")

    print("Current Temperature:{:.1f} C / {:.1f} F    --     Humidity: {}%".format(temperature_c, temperature_f, humidity))

    message = '{"temperature":' + str(temperature_c) + '}'

    start_mqttpublish_reading = time.time()
    message = '{"temperature":' + str(temperature_c) + ', "start_sensor_reading": ' + str(start_sensor_reading) + ', "start_mqttpublish_reading": ' + str(start_mqttpublish_reading) + '}'

    myDeviceShadow.shadowUpdate( message, myShadowUpdateCallback, 5)
    
    stop_mqttpublish_reading = time.time()
    sensor_mqttpublish_latency = stop_mqttpublish_reading - start_mqttpublish_reading
    print(f" MQTT publish latency: {sensor_mqttpublish_latency:.4f} seconds")
    

    time.sleep(10)


