FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm ci --production # ติดตั้งเฉพาะ production dependencies
COPY . .
RUN npm run build

EXPOSE $PORT
CMD ["sh", "-c", "npm run start -- -p $PORT"]