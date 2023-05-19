FROM python:3.10-slim-buster

# Do not cache Python packages
ENV PIP_NO_CACHE_DIR=yes

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# set PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}"

# Initializing new working directory
WORKDIR /code

# Transferring the code and essential data

COPY Crawler ./Crawler
COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock
COPY .env ./.env
RUN pip install pipenv
RUN pipenv install --ignore-pipfile --system

CMD ["python3.10","Crawler/run.py"]