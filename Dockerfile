FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y netcat-openbsd

COPY . .

RUN chmod +x start.sh

CMD ["./start.sh"]
