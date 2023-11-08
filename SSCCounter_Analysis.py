# -*- coding: utf-8 -*-
from Module.data_handler import DataHandler
from Module.yolov3 import Yolov3

import datetime
import time

Data_Handler = DataHandler()

ksize = 20  # 블러 처리에 사용할 커널 크기
obj_color = (0, 255, 0)
classes = ["person"] # 사물 class
size_list = [320, 416, 608] # 입력 사이즈 리스트 (Yolov3에서 사용되는 네트워크 입력 이미지 사이즈), 이 Yolov3는 416 버전

SSCCounter = Yolov3(obj_color=obj_color, classes=classes, size=size_list[1], ksize=ksize)

while True:
    info_deque = Data_Handler.load_data(str("./Data_Folder/nCnt.txt"))
    count, standard_time, refresh = map(str, info_deque)
    if refresh == "1":
        try:
            SSCCounter.yolov3_machine(classes[0], "photo.jpg",'./static/images/analysis.jpg')
        except AttributeError:
            print("시간: {0}  >>>  SSCCount: AttributeError!".format(datetime.datetime.now()))
        except:
            print("시간: {0}  >>>  SSCCount: Error!".format(datetime.datetime.now()))
    time.sleep(1)