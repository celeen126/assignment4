FROM python:3.10.7-slim

ADD main.py .

RUN pip install tabulate

CMD [ "python", "./main.py" ]