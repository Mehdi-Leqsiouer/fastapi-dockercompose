FROM python:3.11

WORKDIR /app

ENV HOST 0.0.0.0

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000
ENV PYTHONPATH "${PYTHONPATH}:/app/src/"
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port","8000"]
