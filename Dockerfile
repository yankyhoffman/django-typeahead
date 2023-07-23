FROM python:3.11.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV UID 1000
ENV GID 1000

WORKDIR /app
RUN mkdir /data
RUN chown -R $UID:$GID /data

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
