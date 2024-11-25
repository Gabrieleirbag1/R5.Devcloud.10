FROM debian:bookworm

RUN mkdir /data
WORKDIR /data
RUN apt-get update && apt-get install -y unzip iputils-ping
COPY test.zip /data

RUN unzip test.zip
RUN chmod +x script.sh

ENTRYPOINT ["./script.sh"]
