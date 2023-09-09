FROM ubuntu:latest

WORKDIR /var/tmp/

# Create a non-root user with UID 1000
RUN useradd -u 1000 -m testuser

RUN apt-get update && apt-get install -y python3 python3-pip wget


COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./terminal.py .
COPY ./app.py .
COPY ./.env .
COPY ./ttyd_install.sh .

RUN ./ttyd_install.sh

RUN apt remove wget -y
RUN rm ttyd_install.sh *.txt

