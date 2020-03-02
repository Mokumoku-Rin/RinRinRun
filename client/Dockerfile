FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY src/package.json /app
RUN npm install
COPY src/. .
RUN npm run build

CMD [ "http-server", "dist" ]