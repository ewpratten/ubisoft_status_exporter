FROM python:3
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./ubisoft_status_exporter.py /app/ubisoft_status_exporter.py

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "ubisoft_status_exporter.py"]