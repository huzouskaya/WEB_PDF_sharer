# Dockerfile для Vue.js
FROM node:16

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы зависимостей
COPY package*.json ./

# Установите зависимости
RUN npm install

# Скопируйте весь проект
COPY . .

# Соберите проект
RUN npm run build

# Установите Nginx для обслуживания статических файлов
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html

# Копируйте конфигурацию Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Запустите Nginx
CMD ["nginx", "-g", "daemon off;"]