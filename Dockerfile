FROM python:3.11-slim-buster

WORKDIR /app

COPY app /app
COPY model/model.pkl /app/model.pkl
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
