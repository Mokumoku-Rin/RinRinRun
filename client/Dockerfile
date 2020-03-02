FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

# CMD [ "http-server", "dist" ]
CMD ["npm", "run", "serve"]
