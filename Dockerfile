FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
run pip install -r requirements.txt

COPY . /app

CMD python run.py 0.0.0.0:5000