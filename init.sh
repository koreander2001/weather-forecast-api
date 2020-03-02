#!/bin/bash


if [[ -e ./django/apps ]]; then
    echo '"./django/apps" exists already.'
else
    echo 'Copying project directory from container.'

    docker run --name tmp -itd django-on-docker /bin/bash
    docker cp tmp:/opt/apps/ ./django/
    docker stop tmp
    docker rm tmp

    echo 'Finish copying.'
fi

