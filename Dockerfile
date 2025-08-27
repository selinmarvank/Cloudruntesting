From python:3.10-slim
WORKDIR /app
COPY app
RUN pip install --no-cache-dir -r

CMD [ "python","app.py" ]

