FROM grafana/grafana:9.3.2

COPY datasource.yml /etc/grafana/provisioning/datasources/datasource.yml

ENV GF_SECURITY_ADMIN_PASSWORD=admin
ENV GF_USERS_ALLOW_SIGN_UP=false
