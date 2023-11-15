FROM python:3.11.1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx wget
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code

WORKDIR /code/WebServer/yolo_data

RUN wget https://pjreddie.com/media/files/yolov3.weights

WORKDIR /code/WebServer

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
