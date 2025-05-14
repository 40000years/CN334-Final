FROM node:18-alpine

# ตั้ง Working Directory
WORKDIR /app

# คัดลอกไฟล์ Dependencies
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./

# ติดตั้ง Dependencies
RUN \
  if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
  elif [ -f package-lock.json ]; then npm ci; \
  elif [ -f pnpm-lock.yaml ]; then yarn global add pnpm && pnpm i --frozen-lockfile; \
  else echo "Lockfile not found." && exit 1; \
  fi

# คัดลอกโค้ดทั้งหมด
COPY . .

# Build Next.js สำหรับ Production
RUN npm run build

# รัน Production Server
CMD ["npm", "run", "start"]