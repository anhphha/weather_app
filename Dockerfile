FROM python:latest

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "vim"]
RUN pip install pytz django pyowm

COPY . /app

EXPOSE 5001
ENTRYPOINT [ "python", "application.py", "weather_app.py"]