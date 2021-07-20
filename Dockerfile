FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/project
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY entrypoint.sh .
COPY . .
ENTRYPOINT["usr/src/project/entrypoint.sh"]