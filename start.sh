docker build -t django2.1 -f ./django/Dockerfile.base ./django
docker-compose down
docker-compose build
docker-compose up -d

