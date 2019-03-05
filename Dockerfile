FROM python:3.5

# Copy in your requirements file

RUN apt-get update && apt-get upgrade

RUN apt-get -y install python3-pip \
        python3-venv apache2 \ 
        libapache2-mod-wsgi-py3 virtualenvwrapper

ADD requirements.txt /requirements.txt

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
COPY sureedu_auth.conf /etc/apache2/sites-available/000-default.conf

RUN mkdir /code/
WORKDIR /code/
ADD . /code/

RUN virtualenv --python=python3 /code/venv

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 775 /code/
RUN chown -R :www-data /code && a2enmod rewrite
RUN chown -R :www-data /code/auth_service/media/
RUN chmod -R 775 /code/auth_service/media

# Apache will listen on this port
EXPOSE 80

# uWSGI will listen on this port
# EXPOSE 8000

# Add any custom, static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=auth_service.settings.production

# uWSGI configuration (customize as needed):
#ENV UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=auth_service/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy


# ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Start uWSGI
#CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]

# start Apache2
CMD ["/usr/sbin/apache2ctl", "-k", ADD requirements.txt /requirements.txt"start"]