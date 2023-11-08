# -*- coding: utf-8 -*-

# ============ Set ============

import cv2
import numpy as np
from datetime import datetime
import time
    
# 변수 지정
previous_time, standard_time, ncnt_people = 0, 0, 0
ksize = 20              # 블러 처리에 사용할 커널 크기

# 사물 class
classes = ["person"]
# classes = ["person",  "bench", "umbrella", "handbag","bottle", "chair", "bed", "dining table",
#            "laptop", "remote", "keyboard", "cell phone", "microwave", "refrigerator", "book"]

# Yolov3 네트워크 블러오기
net = cv2.dnn.readNet("./Yolo_Folder/yolov3.weights", "./Yolo_Folder/yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]



# ============ Function ============ 

# Yolov3 분석 함수
def yolo(frame, size, score_threshold, nms_threshold):
    global ncnt_people
    height, width, channels = frame.shape  # 이미지의 높이, 너비, 채널 받아오기
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (size, size), (0, 0, 0), True, crop=False)  # 네트워크에 넣기 위한 전처리
    net.setInput(blob)  # 전치리된 blob 네트워크에 입력
    outs = net.forward(output_layers)  # 결과 받아오기
    # 각각의 데이터를 저장할 빈 리스트
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.1:
                # 탐지된 객체의 너비, 높이 및 중앙 좌표값 찾기
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # 객체의 사각형 테두리 중 좌상단 좌표값 찾기
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=score_threshold, nms_threshold=nms_threshold)# 후보 박스(x, y, width, height)와 confidence(상자가 물체일 확률) 출력
    ncnt_people = 0
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            class_name = "People"
            label = f"{class_name} {confidences[i]:.2f}"
            color = (0, 255, 0)
            try:  # 인식된 사물 분석 시도
                class_name = classes[class_ids[i]]
                # if class_name = "refrigerator":
                if class_name == "person":
                    ncnt_people += 1  # 사람이 인식되면 ncnt_people 변수 +1
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    cv2.rectangle(frame, (x-1, y), (x + len(class_name) * 13 + 65, y -25), color, -1)
                    cv2.putText(frame, label, (x, y - 8), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
            except IndexError:  # 오류 발생시 pass
                pass
            cv2.imwrite('./static/images/analysis.jpg', frame)  # 이미지 저장
    return frame

def machine():
    global previous_time, ncnt_people, standard_time
    moment_time = str(datetime.now())  # 현재시간 측정
    current_time = int(moment_time[14:16])  # 현재 분 값 저장"temperature": temp, "humidity": hum, "lamp": lamp,
    #if previous_time != current_time:  # 기존 값과 다를 경우
    previous_time = current_time  # 기존 값에 새로운 분 값 저장
    standard_time = moment_time[11:19]  # 기준 시간 설정 (시, 분)

    img = "photo.jpg"  # 이미지 경로
    frame = cv2.imread(img)  # 이미지 읽어오기z
    size_list = [320, 416, 608]  # 입력 사이즈 리스트 (Yolov3에서 사용되는 네트워크 입력 이미지 사이즈)
    frame = yolo(frame=frame, size=size_list[2], score_threshold=0.4, nms_threshold=0.4)  # 이미지 분석
    print("시간: {0}  >>>  SSCCount: {1} 명".format(datetime.now(), ncnt_people))
    with open("nCnt.txt", "w", encoding = "utf8") as report_file:
        report_file.write("{0}/{1}/{2}".format(ncnt_people, standard_time, "0"))
        # print("시간: {0}  >>>    {1} 명".format(datetime.now(), ncnt_people))



# ============ Machine ============ 

while True:
    # TIME = datetime.now().second
    with open("nCnt.txt", "r") as file:
        for line in file.readlines():
            info_list = line.split("/")
            Refresh = info_list[2]
            if Refresh == "1":
                try:
                    machine()
                except AttributeError:
                    print("시간: {0}  >>>  SSCCount: AttributeError!".format(datetime.now()))
                    time.sleep(1)
                except:
                    print("시간: {0}  >>>  SSCCount: Error!".format(datetime.now()))
                    time.sleep(1)