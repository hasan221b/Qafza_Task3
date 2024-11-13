FROM python:3.11.4

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY rfmodel.pkl .
COPY test.py .

RUN pip install -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & sleep 5 && python test.py"]

