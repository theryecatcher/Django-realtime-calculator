FROM python:3
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN mkdir /code
WORKDIR /code
ADD . /code/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN pip install -r requirements.txt
