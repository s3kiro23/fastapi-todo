FROM python:3.11-slim

ARG CONFIG

ARG APP_NAME="fastapi_todo"
ENV PYTHONPATH="/opt/$APP_NAME"

RUN mkdir -p /opt/$APP_NAME /var/log/$APP_NAME

WORKDIR /opt/$APP_NAME

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chown -R www-data:www-data /opt/$APP_NAME /var/log/$APP_NAME

EXPOSE 8080

CMD ["uvicorn", "todo.main:app", "--host", "0.0.0.0", "--port", "8080"]