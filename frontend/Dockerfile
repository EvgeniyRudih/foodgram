FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build
CMD sh -c "mkdir -p /app/result_build && cp -r build/. /app/result_build/"
