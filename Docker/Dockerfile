FROM python:3.9-slim

WORKDIR /app
EXPOSE 8000

COPY Python_app /app
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


CMD ["python", "app.py"]
