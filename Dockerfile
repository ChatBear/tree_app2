FROM python:3.10


WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/main.py ./


COPY app/model_tree.sav ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]