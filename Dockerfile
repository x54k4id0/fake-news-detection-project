FROM node:14-alpine
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk add --update --no-cache py3-numpy py3-pandas@testing
ENV PYTHONPATH=/usr/lib/python3.8/site-packages
RUN pip install numpy nltk openpyxl

WORKDIR /app
COPY ./ .
WORKDIR /app/fake-news-ai
RUN npm run build
WORKDIR /app/server
RUN pip install -r requirements.txt
ENTRYPOINT ["python","server.py"]