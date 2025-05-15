# ใช้ node:18-slim แทน alpine เพื่อความเข้ากันได้
FROM node:18-slim

# ตั้งค่า working directory
WORKDIR /app

# คัดลอก package.json และ package-lock.json
COPY package.json package-lock.json* ./

# ติดตั้ง dependencies (รวม devDependencies สำหรับ build)
RUN npm ci

# คัดลอกโค้ดทั้งหมด
COPY . .

# รัน build
RUN npm run build

# เปิด port ที่กำหนดโดย Render.com
EXPOSE $PORT

# รัน app ด้วย PORT จาก environment variable
CMD ["npm", "run", "start"]