FROM python:3.12.3-alpine

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./src /app

CMD python /app/app.py