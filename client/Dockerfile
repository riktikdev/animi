FROM node:20

RUN apt update -y && apt upgrade -y
WORKDIR /app

COPY package*.json .
RUN ["npm", "install"]

COPY . .

CMD ["npm", "run", "build"]