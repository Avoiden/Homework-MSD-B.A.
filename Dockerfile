FROM python:3

WORKDIR /usr/src/app

EXPOSE 8001

COPY . .

CMD [ "python", "Homework.py" ]
