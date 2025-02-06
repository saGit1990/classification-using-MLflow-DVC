FROM python:3.10.14

# RUN apt update -y  && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3","app.py" ] 