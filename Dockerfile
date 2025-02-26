FROM python:3.14.0a5-bookworm

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD bash -c "flask run --host=0.0.0.0 --port $CONTAINER_PORT --debug"
