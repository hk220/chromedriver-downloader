FROM python:3.11.2

WORKDIR /app

COPY . .

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && pip install . \
    && dpkg-deb -f ./google-chrome-stable_current_amd64.deb version | chromedriver-downloader \
    && unzip chromedriver.zip \
    && cp chromedriver /usr/local/bin
