FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"

RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pipenv install --system --deploy

RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./src /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

VOLUME /vol/web
