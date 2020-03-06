FROM python:3.8.2

ARG SRC_DIR=/src/

COPY ./requirements.txt ${SRC_DIR}
WORKDIR ${SRC_DIR}

RUN pip install -r requirements.txt