FROM node:20-alpine

WORKDIR /app

COPY . .

COPY package.json .

RUN npm install

RUN npm install -g typescript && npm cache clean --force

ENV NODE_ENV production

EXPOSE 3000

CMD ["npm", "run", "prod"]