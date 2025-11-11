# Stage 1: build
FROM node:20-alpine AS builder

WORKDIR /app

# Копируем зависимости
COPY package*.json ./
RUN npm install

# Копируем весь код и билдим
COPY . .
RUN npm run build

# Stage 2: run
FROM node:20-alpine
WORKDIR /app

# Копируем билд и node_modules
COPY --from=builder /app ./

EXPOSE 3000

CMD ["npm", "run", "start"]
