FROM python:3.12

WORKDIR /app/api

RUN pip install poetry==1.7.1
RUN cd /usr/local/bin
RUN ln -s /opt/poetry/bin/poetry
RUN poetry config virtualenvs.in-project true
