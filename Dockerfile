FROM tiangolo/uwsgi-nginx-flask:python3.7

ADD ./app /app
RUN pip install -r /app/requirements.txt
