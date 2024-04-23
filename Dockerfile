FROM python:3.8

WORKDIR /app

ADD . /app
RUN pip install flask

COPY . .

CMD ["python", "./app.py"]
