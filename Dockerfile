FROM ubuntu:latest

RUN useradd -u 1050 -m testuser

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip wget

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY terminal.py .
COPY app.py .
COPY .env .
COPY scripts/. .

RUN ./ttyd_install.sh

RUN apt remove wget -y
RUN rm *.sh *.txt

