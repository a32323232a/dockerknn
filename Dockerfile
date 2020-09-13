### Dockerfile

FROM python:3.7-buster

WORKDIR /app

ADD . /app


RUN pip install -r requirements.txt


CMD ["python","knn_rappor_iris.py"]

