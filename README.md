# SSCCounter-v0.1.0

<div align="center">
<img width="329" alt="image" src="https://github.com/AI-WonYJ/SSCCounter/assets/101448204/4de0bfbc-ec7d-4cec-860f-1e0c37cfc941">

  
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=http%3A%2F%2Fssccounter.shop&count_bg=%2379C83D&title_bg=%23555555&icon=airplayvideo.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
</div>

# SSCCounter Web Page v0.1.0
> **숭실대학교 컴퓨터 동아리 (SSCC: SoongSil ComputingClub)** <br/> **개발기간: 2022.06 ~ 2023.05**

## 배포 주소

> **웹페이지** : [http://www.ssccounter.shop/](http://www.ssccounter.shop/) <br>
> **프론트 서버** : [http://www.ssccounter.shop/uploadfile/](http://www.ssccounter.shop/uploadfile/)<br>
> **Json 요청** : [http://www.ssccounter.shop/ssccounter.json/](http://www.ssccounter.shop/ssccounter.json/)

## 웹개발팀 소개

<div align="center">
  
|      백승우       |          원영진         |                                                                                                               
| :------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: |
|   <img width="160px" src="https://github.com/SSCC-space/SSCCounter/assets/101448204/8f10e608-b397-4425-b39c-9f5fc3be0305" />    |                      <img width="160px" src="https://github.com/AI-WonYJ/SSCCounter/assets/101448204/a7a73b85-ab18-45ca-9326-77290bd7209f" />    |  
|   [@SWtheWhite](https://github.com/SWtheWhite)   |    [@AI-WonYJ](https://github.com/AI-WonYJ)  | 
| 숭실대학교 전자정보공학부 (it융합전공) 4학년 | 숭실대학교 AI융합학부 2학년 |
| SSCC 36th | SSCC 40th |
| Design & Front | HardWare & Web Server |
</div>
  
## 프로젝트 소개

SSCCounter은 동아리방 인원수 카운터 머신입니다. 기존에 많은 사람들이 동아리방에 몇명이나 있는지 문의하는 글이 자주 올라왔었는데, 하루에도 2~3번 씩 올라오는 문의 글로 인해, 중요한 공지 글을 확인하기 힘들었다. 이를 해결하기 위해 동아리방 사용 인원수를 알려주는 머신이 있으면 좋겠다는 요청에 진행된 '2022 여름방학 Smart동방 프로젝트' 중 'nCnt' 개발 프로젝트에서 시작되었습니다. 현재는 Smart동방 프로젝트가 종료됨에 따라 'SSCCounter'라는 이름으로 변경되었으며, 매일 평균 30명 이상이 서비스를 이용하는 동아리 핵심 프로젝트로 진행되고 있습니다. 

#### SSCCounter uses 'YOLOv3 Object Detection Neural Network'.
You can easily check the number of people using the club room by analyzing the images processed by YOLOv3. Thanks to real-time analysis of the club room images, you can instantly verify the number of people without any delays.

#### SSCCounter's website will give you a check-friendly environment.

Our website supports the following component.
1. Last refresh time.
2. Last headcount time
3. Images that can be checked at a glance according to the number of people.

## 시작 가이드
### Requirements
For building and running the application you need:

- [Python 3.11.3](https://www.python.org/downloads/)
- [YOLOv3](https://pjreddie.com/darknet/yolo/)

### Installation
``` bash
$ git clone https://github.com/AI-WonYJ/SSCCounter.git
$ cd SSCCounter/Newest_Version
$ pip install -r requirements.txt
```
#### YOLOv3 Model
```
$ cd YOLO_Folder
```

#### Frontend
```
$ uvicorn SSCCounter_WebServer:app --reload --port=8000 --host=0.0.0.0
```

---

## Stacks 🐈

### Environment
![Windows 11](https://img.shields.io/badge/Windows%2011-0078D4?style=for-the-badge&logo=Windows%2011&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=Ubuntu&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             

### Object Detection Neural Network
![YOLO](https://img.shields.io/badge/YOLOv3-00FFFF?style=for-the-badge&logo=YOLO&logoColor=black)      

### Development
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML3&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS3&logoColor=white)

### Communication
![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)
![Zoom](https://img.shields.io/badge/Zoom-2D8CFF?style=for-the-badge&logo=Zoom&logoColor=white)

---
## 화면 구성 📺

<div align="center">

| 메인 페이지  |  Json 페이지   |
| :-------------------------------------------: | :------------: |
|  <img width="329" src="https://github.com/AI-WonYJ/SSCCounter/assets/101448204/1421f522-7e7a-4503-a1a7-5a9fe036fcc3"/> |  <img width="329" src="https://github.com/AI-WonYJ/SSCCounter/assets/101448204/9b31ea92-45c0-44a6-b316-0c5206d7bc65"/>|  
</div>

---
## 주요 기능 📦

### ⭐️ 동아리 인원수를 숫자와 이미지로 확인 가능
- 숫자뿐만 아니라 이미지 또한 인원수에 따라 변하게 하여 한눈에 확인 가능

### ⭐️ 동아리 홍보 페이지 연계
- 아이콘을 클릭하면 동아리 홍보 페이지나, 소셜 네트워크 페이지로 연결

### ⭐️ 새로고침 버튼
- 간편하게 버튼 하나로 동아리방 인원수를 새로고침

---
## 도입 예정 기능 및 성능 개선 📝

### ⭐️ Web Page 개편
* [ ] UX/UI를 더욱 눈에 띄도록 메인 페이지를 개편

### ⭐️ APP 출시
* [ ] URL 접속이 아닌, APP을 통해 확인할 수 있는 APP 서비스 출시
* [ ] PUSH 알림 등으로 더욱 간편하게 확인

### ⭐️ 동아리방 환경 정보 제공 기능 추가
* [ ] 온도 및 습도 정보와 공기 오염도를 확인할 수 있는 기능 추가

### ⭐️ 로그인 기능 추가
* [ ] 동아리 외부인이 접속할 수 없도록 로그인 기능 추가

### ⭐️ AI 인원수 예측 기능 추가
* [ ] 요일과 날씨, 학교 행사 정보 등을 이용해 동아리방 인원수를 예측

### ⭐️ YOLO 모델 업그레이드
* [ ] YOLOv3 -> YOLOv4, 5, ... 8 중 상위 모델로 업그레이드

---
## 아키텍쳐

### 디렉토리 구조
```bash
├── README.md
├── requirements.txt
├── photo.jpg
├── SSCCounter webpage image.jpg
├── Arduino_Serial_test.py
├── SSCCounter_RP4.py
├── SSCCounter_Analysis.py
├── SSCCounter_WebServer.py
├── Module
│   ├── data_handler.py
│   ├── yolov3.py
├── Data_Folder
│   ├── nCnt.txt
├── Yolo_Folder
│   ├── yolov3.cfg
│   ├── yolov3.md : yolov3.weight 다운로드 방법
├── templates
│   ├── index(Ver_8).html : 메인 webpage
│   ├── docs.html : 개발자용 webpage
│   ├── image.html
│   ├── manager.html
│   ├── new.html
│   ├── test.html
└── static
    ├── css
    │   ├── main(Ver_2).css
    │   ├── main.css
    │   └── new.css
    └── images
        ├── 0 people.png
        ├── 1 people.png
        ├── 2 people.png
        ├── 3 people.png
        ├── 4 people.png
        ├── 5 people.png
        ├── 6 people.png
        ├── people.png
        ├── Kakao_lion.png
        ├── SSCC_logo.png
        ├── SSCC_logo_rev.png
        ├── discord.png
        ├── facebook.png
        ├── humidity.png
        ├── instagram.png
        ├── kakao.png
        ├── logo.png
        ├── notion.png
        ├── temperature.png
        ├── analysis.jpg
        ├── analysis3.jpg
        ├── analysis_outdoor.jpg
        └── photo_out.jpg

```
