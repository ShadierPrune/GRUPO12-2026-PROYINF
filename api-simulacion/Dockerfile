FROM node:20-alpine

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

# Ejecutamos el script de desarrollo que lee directamente el .ts
CMD ["npm", "run", "dev"]