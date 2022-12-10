FROM python:3.10

ENV FLASK_RUN_HOST=127.0.0.1
ENV FLASK_RUN_PORT=5000

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install net-tools

CMD [ "python", "./main.py" ]

# docker run -d -p 8080:5000 --name homework hw5:<version>