FROM python:3.5

# Copy in your requirements file

RUN apt-get update && apt-get upgrade

RUN apt-get -y install python3-pip \
        python3-venv nginx \ 
        supervisor \
        virtualenv

# setup all the configfiles
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY sureedu_auth.conf /etc/nginx/sites-available/default

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)

RUN mkdir /code


RUN virtualenv --python=python3 /code/venv

COPY src/requirements.txt /code/
RUN /code/venv/bin/pip install --no-cache-dir -r /code/requirements.txt

ADD . /code/
WORKDIR /code/src
# Nginx will listen on this port
EXPOSE 80 443

# uWSGI will listen on this port
# EXPOSE 8000

# Add any custom, static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=auth_service.settings.production

# uWSGI configuration (customize as needed):
#ENV UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=auth_service/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Start uWSGI
#CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]

# start Supervisord
CMD ["supervisord", "-n"]
#CMD ["bash", "-c", "service apache2 start"]