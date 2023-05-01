FROM nginxinc/nginx-unprivileged:alpine

COPY cyberchef /usr/share/nginx/html

# spider = only check if file exists, don't donwnload
HEALTHCHECK CMD wget --quiet --spider localhost:8080
