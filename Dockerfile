FROM python:3.7-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./source /app/source

WORKDIR /app/source

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD ["python3" ,"main.py"]
