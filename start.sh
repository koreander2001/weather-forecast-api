docker build -t django2.1 -f ./django/Dockerfile.base ./django
/usr/local/bin/docker-compose down
/usr/local/bin/docker-compose build
/usr/local/bin/docker-compose up -d

