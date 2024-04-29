FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# set workdir
WORKDIR /app

# install dependeddcies
RUN pip install --upgrade pip
COPY ./requirements.txt ./constraints.txt /app/
RUN pip install -r requirements.txt -c constraints.txt

# copy project
COPY . /app
