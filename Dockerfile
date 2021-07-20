FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/project
RUN apt-get update \
    && apt-get install -yyq netcat
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY entrypoint.sh ./

ENTRYPOINT ["/usr/src/project/entrypoint.sh"]