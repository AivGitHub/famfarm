FROM nginx:latest

# Core of Nginx
COPY settings/sites-available/* /etc/nginx/sites-available/

# Params and additional resolvers
COPY settings/additional/* /etc/nginx/

# Move certificates
RUN mkdir -p /var/lib/famfarm/certificates/
COPY settings/certificates/* /var/lib/famfarm/certificates/

RUN mkdir -p /etc/nginx/sites-enabled/ \
    && ln -s /etc/nginx/sites-available /etc/nginx/sites-enabled \
    && rm /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
