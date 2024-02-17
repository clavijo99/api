FROM python:3.8.0
ENV PYTHONUNBUFFERED=1

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
        python-psycopg2 \
        gettext \
 && rm -rf /var/lib/apt/lists/*

# Setup workdir
RUN mkdir /src
WORKDIR /src

COPY ./scripts/command-dev.sh /scripts/
RUN chmod +x /scripts/command-dev.sh

# Python dependencies
COPY requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt

COPY . /src