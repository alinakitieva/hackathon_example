FROM python:3.9

WORKDIR /app

COPY ./app /app
COPY ./model/model.pkl /app/model.pkl
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "api.py"]
