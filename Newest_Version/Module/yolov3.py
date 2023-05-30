# -*- coding: utf-8 -*-
from Module.data_handler import DataHandler

import cv2
import numpy as np
import datetime

Data_Handler = DataHandler()

# Yolov3 네트워크 블러오기
net = cv2.dnn.readNet("./Yolo_Folder/yolov3.weights", "./Yolo_Folder/yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

class Yolov3:
    def __init__(self, obj_color, classes, size:int, ksize):
        self.reanalysis_time = 0
        self.ncnt_people = 0
        self.ksize = ksize#20  # 블러 처리에 사용할 커널 크기
        self.obj_color = obj_color#(0, 255, 0)
        self.classes = classes
        self.size = size
        
    def yolov3_analysis(self, object:str, file_path:str, frame, size:int, score_threshold:float, nms_threshold:float):
        height, width, channel = frame.shape # 이미지의 높이, 너비, 채널 받아오기
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (size, size), (0, 0, 0), True, crop=False)  # 네트워크에 넣기 위한 전처리
        net.setInput(blob)  # 전치리된 blob 네트워크에 입력
        outs = net.forward(output_layers)  # 결과 받아오기
        # 각각의 데이터를 저장할 빈 리스트
        class_ids, confidences, boxes = [], [], []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.1:
                    # 탐지된 객체의 너비, 높이 및 중앙 좌표값 찾기
                    center_x = int(detection[0] * width); center_y = int(detection[1] * height)
                    w = int(detection[2] * width); h = int(detection[3] * height)
                    # 객체의 사각형 테두리 중 좌상단 좌표값 찾기
                    x = int(center_x - w / 2); y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=score_threshold, nms_threshold=nms_threshold)# 후보 박스(x, y, width, height)와 confidence(상자가 물체일 확률) 출력
        self.ncnt_people = 0
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = f"{object} {confidences[i]:.2f}"
                try:  # 인식된 사물 분석
                    class_name = self.classes[class_ids[i]]
                    if class_name == object:
                        self.ncnt_people += 1  # 사람이 인식되면 ncnt_people 변수 +1
                        cv2.rectangle(frame, (x, y), (x + w, y + h), self.obj_color, 2)
                        cv2.rectangle(frame, (x-1, y), (x + len(class_name) * 13 + 65, y -25), self.obj_color, -1)
                        cv2.putText(frame, label, (x, y - 8), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
                except IndexError:  # 오류 발생시 pass
                    pass
        cv2.imwrite(file_path, frame)  # 이미지 저장
        reanalysis_time = datetime.datetime.now().strftime('%H:%M:%S')  # 현재시간 측정
        return reanalysis_time
    
    def yolov3_machine(self, find_object, img_path, save_analysis_img_path):
        frame = cv2.imread(img_path)  # 이미지 읽어오기
        reanalysis_time = self.yolov3_analysis(find_object, save_analysis_img_path, frame=frame, size=self.size, score_threshold=0.4, nms_threshold=0.4)  # 이미지 분석
        Data_Handler.write_data("./Data_Folder/nCnt.txt", "w", "{0}/{1}/{2}".format(self.ncnt_people, reanalysis_time, "0"))
        print("시간: {0}  >>>  SSCCount: {1} 명".format(datetime.datetime.now(), self.ncnt_people))