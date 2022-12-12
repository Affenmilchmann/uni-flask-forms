FROM python:latest

ENV FLASK_RUN_HOST=127.0.0.1
ENV FLASK_RUN_PORT=5000

WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /usr/src/app

CMD [ "python3", "./main.py" ]