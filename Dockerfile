FROM python:3.9

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN apt-get update -y
RUN apt-get install -y libsox-fmt-mp3
#CMD tail -f /dev/null
