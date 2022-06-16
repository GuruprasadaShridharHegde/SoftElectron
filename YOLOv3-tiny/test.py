import os
import serial
import time
from time import sleep
import cv2
import numpy as np
import RPi.GPIO as GPIO
from gpiozero import LightSensor
import pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.500)
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
ldr = LightSensor(4)  # gpio 4
GPIO.setup(27, GPIO.IN)
port.write(b'AT\r')
rcv = port.read(10)
print(rcv)
time.sleep(1)





net = cv2.dnn.readNetFromDarknet("/home/p1/Desktop/SoftElectron/yolov3-tiny.cfg",
                                 "/home/p1/Desktop/SoftElectron/yolov3-tiny.weights")


# net=cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes = []
with open("/home/p1/Desktop/SoftElectron/labels.txt", "r") as f:
    classes = f.read().splitlines()

# print(classes)

cap = cv2.VideoCapture(0)
# img=cv2.imread('image.jpg')

while True:
    
    ## Laser and Fire
    if (ldr.value < 0.9)==False:
            #buzzer.on()
            print('Laser intervention Alert, sending sms')
            port.write(b"AT+CMGF=1\r")
            print("Text Mode Enabled…")
            time.sleep(3)
            port.write(b'AT+CMGS="9482152447"\r')
            msg = "Laser intervention Alert"
                  #print("sending message….")
            time.sleep(3)
            port.reset_output_buffer()
            time.sleep(1)
            port.write(str.encode(msg+chr(26)))
            time.sleep(3)
            print("message sent")
            pygame.mixer.music.load("/home/p1/Desktop/SoftElectron/04.wav")
            pygame.mixer.music.play()
            
    elif (GPIO.input(27))==False:
            print('Fire Detection Alert, sending sms')
            port.write(b"AT+CMGF=1\r")
            print("Text Mode Enabled…")
            time.sleep(3)
            port.write(b'AT+CMGS="9482152447"\r')
            msg = "Fire Detection Alert!!"
            print("sending message….")
            time.sleep(3)
            port.reset_output_buffer()
            time.sleep(1)
            port.write(str.encode(msg+chr(26)))
            time.sleep(3)
            print("message sent")
            pygame.mixer.music.load("/home/p1/Desktop/SoftElectron/03.wav")
            pygame.mixer.music.play()

    else:
        print("Farmland is secure")
        time.sleep(3)
            
    
    
   
 
    
    
    
    
#Camera code    
    _, img = cap.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(
        img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)

    # for b in blob:
    #     for n,img_blob in enumerate(b):
    #         cv2.imshow(str(n),img_blob)

    net.setInput(blob)

    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x-w/2)
                y = int(center_y-h/2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    # print(len(boxes))
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    # print(indexes.flatten())

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            # for i in range(i<100):
            if classes[class_ids[i]] == 'bird':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/bird.mp3")
                pygame.mixer.music.play()
                print('Bird Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Bird Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'cat':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/cat.mp3")
                pygame.mixer.music.play()
                print('Cat Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Cat Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'dog':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/dog.mp3")
                pygame.mixer.music.play()
                print('Dog Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Dog Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'horse':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/horse.mp3")
                pygame.mixer.music.play()
                print('Horse Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Horse Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'sheep':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/sheep.mp3")
                pygame.mixer.music.play()
                print('Sheep Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Sheep Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'cow':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/cow.mp3")
                pygame.mixer.music.play()
                print('Cow Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Cow Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'elephant':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/elephant.mp3")
                pygame.mixer.music.play()
                print('Elephant Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Elephant Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'bear':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/bear.mp3")
                pygame.mixer.music.play()
                print('Bear Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Bear Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'zebra':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/zebra.mp3")
                pygame.mixer.music.play()
                print('Zebra Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Zebra Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            if classes[class_ids[i]] == 'giraffe':
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/giraffe.mp3")
                pygame.mixer.music.play()
                print('Giraffe Intrusion Alert, sending sms')
                port.write(b"AT+CMGF=1\r")
                time.sleep(3)
                port.write(b'AT+CMGS="9482152447"\r')
                msg = "Giraffe Intrusion Alert"
                      #print("sending message….")
                time.sleep(3)
                port.reset_output_buffer()
                time.sleep(1)
                port.write(str.encode(msg+chr(26)))
                time.sleep(3)
                time.sleep(20)
            """if classes[class_ids[i]] == 'person':
                # time.sleep(5)
                pygame.mixer.music.load(
                    "/home/p1/Desktop/SoftElectron/person.mp3")
                pygame.mixer.music.play()
                print('Dear farmer, your farmland is secure')
                time.sleep(20)"""
            confidence = str(round(confidences[i], 2))
            # print(confidence)
            color = colors[i]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, label + " " + confidence,
                        (x, y+20), font, 2, (255, 255, 255), 2)

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
