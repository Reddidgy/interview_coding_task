FROM ubuntu:latest

# Install Python and Pip
RUN apt-get update && apt-get install -y python3 python3-pip wget

WORKDIR /app

COPY requirements.txt .
COPY terminal.py .
COPY .env .
COPY scripts/ttyd_install.sh .
copy app.py ./

# Install dependencies from requirements.txt
RUN pip3 install -r requirements.txt

RUN ./ttyd_install.sh
RUN rm requirements.txt ttyd_install.sh

RUN useradd testuser -p 1234567

## Replace the TG_TOKEN value in tg_ubuntu.py with the value of TGBOT_TOKEN environment variable
#RUN sed -i 's/TG_TOKEN/'"$TGBOT_TOKEN"'/g' tg_ubuntu.py

# Set the default command to run the Python script
CMD ["ttyd", "python3", "terminal.py"]
