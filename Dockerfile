FROM python:buster

COPY . /btre

WORKDIR /btre

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000