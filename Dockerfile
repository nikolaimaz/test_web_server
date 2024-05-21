FROM python:3.9-alpine

WORKDIR /app

RUN apk update && apk add --no-cache \
    build-base \
    linux-headers \
    pcre-dev 
    
COPY . .

RUN  pip install --upgrade pip && pip install -r requirements.txt && rm -rf requirements.txt


EXPOSE 5000

CMD ["uwsgi", "--ini", "uwsgi.ini"]