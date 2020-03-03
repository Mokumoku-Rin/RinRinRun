FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app
COPY ./src/package*.json ./
RUN npm install
# 本番用にコードを作成している場合
# RUN npm install --only=production

# CMD [ "http-server", "dist" ]
CMD ["npm", "run", "serve"]
