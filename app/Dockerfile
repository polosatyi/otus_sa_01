FROM python:3.8-alpine

WORKDIR /srv/

COPY server.py /srv/
COPY requirements.txt /srv/

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["python", "server.py"]
