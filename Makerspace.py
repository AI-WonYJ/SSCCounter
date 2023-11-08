#  -*- coding: utf-8 -*-
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()
    
# ============ Function ============

Accessor, Today= "NULL", "Restart"

def Check():
    global ncnt_people, standard_time
    with open("nCnt.txt", "r") as file:
        for line in file.readlines():
            info_list = line.split("/")
            ncnt_people = info_list[0]
            standard_time = info_list[1]

def Accessor_Count():
    if Today != datetime.now().date():
        with open("Daily_Accessor.txt", "a", encoding = "utf8") as Accessor_Report_File:
            Accessor_Report_File.write("{0}    /    {1}명".format(Today, Accessor))
        Accessor = 0
        Today == datetime.now().date()

    Accessor += 1
    with open("Today_Accessor.txt", "w", encoding = "utf8") as report_file:
        report_file.write("{0}/{1}".format(datetime.now(), Accessor))

# ============ Machine ============

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
# , ncnt_people: str, current_time: str, standard_time: str):
async def Page(request: Request):
    global ncnt_people, standard_time, temp, hum, lamp 
    Check()
    Accessor_Count()
    current_time = str(datetime.now() )[0:21]  # 필요한 부분 가공
    print(current_time)
    if int(ncnt_people) <= 6:
        countable = 1
    else:
        countable = 0
    # FastAPI로 new.html에 변수 값 전달
    return templates.TemplateResponse("index(Ver_8).html", {"request": request, "Accessor": Accessor, "People_Count": int(ncnt_people), "Countable": countable, "last_time": current_time, "get_time": current_time, "Get_Time": standard_time})

# @app.get("/Image", response_class=HTMLResponse)
# # , ncnt_people: str, current_time: str, standard_time: str):
# async def Page(request: Request):
#     return templates.TemplateResponse("image.html", {"request": request})

@app.get("/nCnt")
async def nCnt():
    global ncnt_people, standard_time
    Check()
    Accessor_Count()
    current_time = str(datetime.now() )[0:21]  # 필요한 부분 가공
    print(ncnt_people)
    return {"people_count": ncnt_people, "last_time": current_time, "get_time": standard_time}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)

    return {"filename": file.filename}