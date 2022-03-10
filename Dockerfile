FROM registry.access.redhat.com/ubi8/python-39

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY RestApi_POC_django /app

RUN rm -rf /opt/app-root/lib64/python3.9/site-packages/django/db/backends/postgresql/introspection.py

RUN ls /opt/app-root/lib64/python3.9/site-packages/django/db/backends/postgresql

COPY ./introspection.py /opt/app-root/lib64/python3.9/site-packages/django/db/backends/postgresql/introspection.py

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
