FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY client/src/package*.json ./
RUN npm install
COPY client/src/. .
RUN npm run build

CMD [ "http-server", "dist" ]