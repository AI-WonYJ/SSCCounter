#  -*- coding: utf-8 -*-
from Module.data_handler import DataHandler
    
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import datetime

app = FastAPI()#docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

Data_Handler = DataHandler()
info_deque = Data_Handler.load_data(str("./Data_Folder/nCnt.txt"))

@app.get("/", response_class=HTMLResponse)
async def Page(request: Request):
    count, standard_time, refresh = map(str, info_deque)
    refresh_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if int(count) <= 6:
        countable = 1
    else:
        countable = 0
    return templates.TemplateResponse("index(Ver_8).html", {"request": request, "People_Count": int(count), "Countable": countable, "last_time": refresh_time, "get_time": refresh_time, "Get_Time": standard_time})

@app.get("/ssccounter.json")
async def datajson():
    count, standard_time, refresh = map(str, info_deque)
    refresh_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {"People count": count, "Refresh time": refresh_time, "Last Image analysis time": standard_time}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    Data_Handler.write_data("./Data_Folder/nCnt.txt", "w", "0/0/{0}".format("1"))
    Data_Handler.write_file(file.filename, "wb", contents)
    return {"filename": file.filename}