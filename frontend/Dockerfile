# === builder stage ===
FROM node:20-alpine AS builder
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Сборка проекта
RUN npm run build
# Экспорт статических файлов в папку "out"
RUN npm run export

# === nginx stage ===
FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/
# Копируем статические файлы в nginx
COPY --from=builder /app/out /usr/share/nginx/html

EXPOSE 80
ENV PORT 80
