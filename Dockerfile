FROM python:3.8

COPY ./requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app

COPY ./main.py ./main.py
COPY ./app /app
COPY ./migrations ./migrations
ENV FLASK_APP main.py

EXPOSE 5000