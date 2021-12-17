FROM python:3

COPY . /opt/app

WORKDIR /opt/app

RUN pip install --upgrade -r requirements.txt

COPY ./entrypoint.sh /opt/app/entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]