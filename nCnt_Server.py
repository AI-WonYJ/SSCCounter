#  -*- coding: utf-8 -*-
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI(docs_url=None, redoc_url=None)
    

SSCCount, Standard_Time, Refresh = 0, 0, 0#, temp, hum, lamp
# ============ Function ============
def check():
    global SSCCount, Standard_Time, Refresh
    with open("nCnt.txt", "r") as file:
        for line in file.readlines():
            info_list = line.split("/")
            SSCCount, Standard_Time, Refresh = map(str, info_list)
            # SSCCount = info_list[0]
            # Standard_Time = info_list[1]

# ============ Machine ============

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
# , SSCCount: str, current_time: str, Standard_Time: str):
async def Page(request: Request):
    global SSCCount, Standard_Time, Refresh#, temp, hum, lamp 
    check()
    current_time = str(datetime.now() )[0:21]  # 필요한 부분 가공
    print(current_time)
    if int(SSCCount) <= 6:
        countable = 1
    else:
        countable = 0
    # FastAPI로 new.html에 변수 값 전달
    return templates.TemplateResponse("index(Ver_8).html", {"request": request, "People_Count": int(SSCCount), "Countable": countable, "last_time": current_time, "get_time": current_time, "Get_Time": Standard_Time})

@app.get("/SSCCounter.json")
async def nCnt():
    global SSCCount, Standard_Time#, temp, hum, lamp 
    check()
    current_time = str(datetime.now() )[0:21]  # 필요한 부분 가공
    print(SSCCount)
    return {"people_count": SSCCount, "last_time": current_time, "get_time": Standard_Time}

@app.get("/manager.page", response_class=HTMLResponse)
async def Page(request: Request):
    global SSCCount, Standard_Time, Refresh#, temp, hum, lamp 
    check()
    current_time = str(datetime.now() )[0:21]  # 필요한 부분 가공
    print(current_time)
    if int(SSCCount) <= 6:
        countable = 1
    else:
        countable = 0
    # FastAPI로 new.html에 변수 값 전달
    return templates.TemplateResponse("manager.html", {"request": request, "People_Count": int(SSCCount), "Countable": countable, "last_time": current_time, "get_time": current_time, "Get_Time": Standard_Time})

@app.get("/manager.Image", response_class=HTMLResponse) 
# , SSCCount: str, current_time: str, Standard_Time: str):
async def Page(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})

@app.get("/manager.docs", response_class=HTMLResponse)
async def Page(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    global SSCCount, Standard_Time
    with open("nCnt.txt", "w", encoding = "utf8") as report_file:
        report_file.write("{0}/{1}/{2}".format(SSCCount, Standard_Time, "1"))
    with open(file.filename, "wb") as f:
        f.write(contents)

    return {"filename": file.filename}