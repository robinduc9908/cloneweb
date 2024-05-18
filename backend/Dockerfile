FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app/backend

COPY ./requirements.txt /app/backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]