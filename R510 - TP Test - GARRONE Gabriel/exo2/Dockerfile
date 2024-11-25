FROM debian:bookworm-slim

RUN mkdir /data && \
    apt-get update && \
    apt-get install -y unzip iputils-ping && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /data

COPY test.zip /data

RUN unzip test.zip && chmod +x script.sh

ENTRYPOINT ["./script.sh"]
