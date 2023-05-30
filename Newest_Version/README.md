# SSCCounter-3rd

<div align="center">
<img width="329" alt="image" src="https://github.com/AI-WonYJ/SSCCounter/assets/101448204/4de0bfbc-ec7d-4cec-860f-1e0c37cfc941">

  
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=http%3A%2F%2Fssccounter.shop&count_bg=%2379C83D&title_bg=%23555555&icon=airplayvideo.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
</div>

# SSCCounter Web Page v3.0
> **숭실대학교 컴퓨터 동아리 (SSCC: SoongSil ComputingClub)** <br/> **개발기간: 2022.06 ~ 2023.05**

## 배포 주소

> **웹페이지** : [http://www.ssccounter.shop/](http://www.ssccounter.shop/) <br>
> **프론트 서버** : [http://www.ssccounter.shop/uploadfile/](http://www.ssccounter.shop/uploadfile/)<br>
> **Json 요청** : [http://www.ssccounter.shop/ssccounter.json/](http://www.ssccounter.shop/ssccounter.json/)

## 웹개발팀 소개

<div align="center">
  
|      백승우       |          원영진         |                                                                                                               
| :------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: |
|   <img width="160px" src="https://avatars.githubusercontent.com/u/44691277?v=4" />    |                      <img width="160px" src="https://github.com/AI-WonYJ/SSCCounter/assets/101448204/a7a73b85-ab18-45ca-9326-77290bd7209f" />    |  
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
| 메인 페이지  |  소개 페이지   |
| :-------------------------------------------: | :------------: |
|  <img width="329" src="https://user-images.githubusercontent.com/50205887/208036155-a57900f7-c68a-470d-923c-ff3c296ea635.png"/> |  <img width="329" src="https://user-images.githubusercontent.com/50205887/208036645-a76cf400-85bc-4fa2-af72-86d2abf61366.png"/>|  
| 강좌 소개 페이지   |  강의 영상 페이지   |  
| <img width="329" src="https://user-images.githubusercontent.com/50205887/208038737-2b32b7d2-25f4-4949-baf5-83b5c02915a3.png"/>   |  <img width="329" src="https://user-images.githubusercontent.com/50205887/208038965-43a6318a-7b05-44bb-97c8-b08b0495fba7.png"/>     |

---
## 주요 기능 📦

### ⭐️ 강좌 선택 및 강의 영상 시청 기능
- Scratch, Python 2개 강좌 및 각 강좌마다 10개 가량의 강의 영상 제공
- 추후 지속적으로 강좌 추가 및 업로드 예정

### ⭐️ 강의 관련 및 단체에 대한 자유로운 댓글 작성 가능
- Disqus를 이용하여 강의 관련 질문이나 단체에 대한 질문 작성 가능

### ⭐️ 이어 학습하기 기능
- Cookie 기능을 이용하여 이전에 학습했던 내용 이후부터 바로 학습 가능

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