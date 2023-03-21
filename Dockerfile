FROM python:3.11.2

WORKDIR /app

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt update \
    && apt install -y ./google-chrome-stable_current_amd64.deb
