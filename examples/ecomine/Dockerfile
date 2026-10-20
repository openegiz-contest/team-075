FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir "paho-mqtt>=2,<3"
COPY examples/ecomine/ /app/
