# ---------- 1. СТАДИЯ СБОРКИ ----------
FROM node:20-alpine AS builder

WORKDIR /app

# Копируем package.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm ci

# Копируем весь проект
COPY . .

# Собираем Next.js в продакшене
RUN npm run build


# ---------- 2. СТАДИЯ ЗАПУСКА ----------
FROM node:20-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production

# В продакшене Next.js может работать в standalone режиме
COPY --from=builder /app/.next/standalone ./standalone
COPY --from=builder /app/.next/static ./standalone/.next/static
COPY --from=builder /app/public ./standalone/public

EXPOSE 80

# Запуск next standalone сервера
CMD ["node", "standalone/server.js"]
