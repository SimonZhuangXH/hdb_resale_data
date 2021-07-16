FROM python:3.9

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "src/hdb_resale_data/main/main.py"]
