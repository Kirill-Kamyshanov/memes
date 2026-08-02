FROM python:3.13.14-alpine3.23
COPY . /framework
WORKDIR /framework
RUN pip install -r requirements.txt
