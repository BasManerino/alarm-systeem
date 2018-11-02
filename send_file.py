import time
import RPi.GPIO as io
import RPi.GPIO as GPIO
import socket
io.setmode(io.BCM)
     

UDP_IP = "145.89.205.211"

UDP_PORT = 5005
GPIO

door_pin = 23
light_pin = 25
printed = 0
loop = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)


def reset():
    def ontvang(MESSAGE, UDP_IP, UDP_PORT):
        print("UDP target IP:", UDP_IP)

        print("UDP target port:", UDP_PORT)

        print("message:", MESSAGE)

        sock = socket.socket(socket.AF_INET,  # Internet

        socket.SOCK_DGRAM)  # UDP


        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

    #io.cleanup()   
    io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP) # activate input with PullUp
    io.setup(light_pin,io.OUT)
    io.output(light_pin, io.LOW)
    while True:
        if io.input(door_pin):
            MESSAGE = "OPEN"
            io.output(light_pin, io.HIGH)
            ontvang(MESSAGE, UDP_IP, UDP_PORT)  
        else:
            continue
           
    #time.sleep(0.5)

    io.cleanup()
while True:
    if GPIO.input(24):
        reset()
    