
import paho.mqtt.client as mqtt #import the client1

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    public_client.publish("siloAnomaly/1", msg.payload)

broker_address="0.0.0.0"

public_broker_address="broker.hivemq.com" #use external broker

client = mqtt.Client() #create new instance
public_client = mqtt.Client()



def main():
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, 1883, 60)
    client.loop_forever()

    public_client.connect(public_broker_address, 1883, 60)
    public_client.loop_forever()
    
if __name__ == '__main__':
    main()