FROM nginxinc/nginx-unprivileged:alpine

COPY cyberchef /usr/share/nginx/html
