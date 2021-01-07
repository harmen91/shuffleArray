FROM python:3.9.1
RUN apt-get update
RUN pip3 install numpy==1.19.5
WORKDIR /home
COPY shuffleArray.py .

