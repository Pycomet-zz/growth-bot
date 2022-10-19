#pull official base image
FROM python:3.10.8-slim-buster


#set working directory
WORKDIR /

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUMBUFFERED 1

# #install system dependencies
# RUN apt-get update \
#     && apt-get -y install netcat gcc \
#     && apt-get clean

# install python dependenciess
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

EXPOSE 8000

CMD [ "python", "bot.py" ]
