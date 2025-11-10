FROM FROM node:20-alpine AS builder
# ARG REACT_APP_CEC_API
# ENV REACT_APP_CEC_API=${REACT_APP_CEC_API}
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build


FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/
COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80
ENV PORT 80