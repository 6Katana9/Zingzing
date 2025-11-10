# builder stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build   # теперь автоматически создаст /app/out

# nginx stage
FROM nginx:alpine
# COPY default.conf /etc/nginx/conf.d/
# COPY --from=builder /app/out /usr/share/nginx/html
RUN chmod -R 755 /usr/share/nginx/html  # чтобы nginx мог читать
EXPOSE 80
