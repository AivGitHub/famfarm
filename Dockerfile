# syntax=docker/dockerfile:1
FROM python:3.8.10

# Arguments
ARG APP_USER=www-data
ARG WORKDIR=/www
ARG DEBIAN_FRONTEND=noninteractive

# Environ
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Files management
COPY . ${WORKDIR}
WORKDIR ${WORKDIR}

# Install linux dependencies
RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends \
        build-essential \
        libpq-dev \
        libpcre3 \
        libpcre3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install python environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install python dependencies
# TODO: Create user or use --no-warn-root-privileges
RUN pip install --upgrade pip \
    && pip install \
        --no-cache-dir \
        -r requirements.txt
