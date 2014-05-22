from debian:wheezy

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y gcc python-dev python-pip git procps curl libpq-dev
RUN pip install -U pip

RUN mkdir /src
ADD requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install -r requirements.txt

ADD . /src/

EXPOSE 80

CMD ["python", "server.py"]
