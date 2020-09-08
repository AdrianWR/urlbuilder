FROM python:3.6.9-buster
LABEL maintainer="adrian.w.roque@gmail.com"

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY urlbuilder.py ./

ARG CHROMIUM_VERSION=83.0.4103.116-1~deb10u3
ARG CHROMEDRIVER_VERSION=83.0.4103.39

RUN apt-get update && apt-get install -y chromium=$CHROMIUM_VERSION
RUN curl -LO https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/lib/chromium-browser						&& \
    ln -s /usr/lib/chromium-browser/chromedriver /usr/local/bin
RUN pip install --no-cache-dir -r requirements.txt

ENV PROJECT_ID	for-adrian
ENV TABLE_ID	urls.articles
ENV GOOGLE_APPLICATION_CREDENTIALS /usr/src/app/credentials.json

ENTRYPOINT ["python", "./urlbuilder.py"]
CMD ["protein", "medicine", "virus", "20"]
