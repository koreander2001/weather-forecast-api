FROM python:3.8

ENV APP_PATH /opt/apps
WORKDIR $APP_PATH

COPY ./requirements.txt ./
RUN pip install --upgrade pip & \
    pip install --no-cache-dir -r ./requirements.txt
