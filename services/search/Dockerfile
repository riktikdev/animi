FROM python:3.11.4

RUN apt update -y && apt upgrade -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "main.py"]