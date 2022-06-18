import os
import time
from time import sleep
import cv2
import numpy as np
import pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.400)
net = cv2.dnn.readNetFromDarknet("C:/Users/Guruprasada/Desktop/YOLOv3-tiny/yolov3-tiny.cfg",
                                 "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/yolov3-tiny.weights")


# net=cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes = []
with open("C:/Users/Guruprasada/Desktop/YOLOv3-tiny/labels.txt", "r") as f:
    classes = f.read().splitlines()

# print(classes)

cap = cv2.VideoCapture(0)
# img=cv2.imread('image.jpg')

while True:
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
            """if classes[class_ids[i]] == 'bird':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/bird.mp3")
                pygame.mixer.music.play()
                print('Bird Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'cat':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/cat.mp3")
                pygame.mixer.music.play()
                print('Cat Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'dog':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/dog.mp3")
                pygame.mixer.music.play()
                print('Dog Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'horse':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/horse.mp3")
                pygame.mixer.music.play()
                print('Horse Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'sheep':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/sheep.mp3")
                pygame.mixer.music.play()
                print('Sheep Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'cow':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/cow.mp3")
                pygame.mixer.music.play()
                print('Cow Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'elephant':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/elephant.mp3")
                pygame.mixer.music.play()
                print('Elephant Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'bear':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/bear.mp3")
                pygame.mixer.music.play()
                print('Bear Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'zebra':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/zebra.mp3")
                pygame.mixer.music.play()
                print('Zebra Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'giraffe':
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/giraffe.mp3")
                pygame.mixer.music.play()
                print('Giraffe Intrusion Alert')
                time.sleep(20)
            if classes[class_ids[i]] == 'person':
                # time.sleep(5)
                pygame.mixer.music.load(
                    "C:/Users/Guruprasada/Desktop/YOLOv3-tiny/person.mp3")
                pygame.mixer.music.play()
                print('Dear farmer, your farmland is secure')
                time.sleep(20)"""
            confidence = str(round(confidences[i], 2))
            # print(confidence)
            color = colors[i]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, label + " " + confidence,
                        (x, y+20), font, 2, (100, 100, 100), 2)

    
    cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN) 
    cv2.setWindowProperty("Image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN) 
    cv2.imshow("Image", img)


    #cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
