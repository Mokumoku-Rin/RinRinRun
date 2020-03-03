FROM python:3.8.2-alpine

ARG SRC_DIR=/src/

COPY ./requirements.txt ${SRC_DIR}
WORKDIR ${SRC_DIR}

RUN apk --no-cache add gcc python3-dev libc-dev make && pip install -r requirements.txt
