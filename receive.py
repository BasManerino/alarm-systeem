import time
import RPi.GPIO as GPIO
import socket

UDP_IP = "145.89.205.211"
UDP_PORT = 5005

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

sock = socket.socket(socket.AF_INET,  # Internet
socket.SOCK_DGRAM)  # UDP


sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print("received message: ", data)
    command = str(data)
    if command=='OPEN':
        GPIO.output(23, True)
        if GPIO.input(24):
            GPIO.output(23, False)
            #continue
            break
            GPIO.cleanup()
        #else:
            #GPIO.output(23, True)
            
            
