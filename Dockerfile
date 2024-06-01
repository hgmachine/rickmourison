FROM ubuntu

RUN apt update && apt-get update
RUN apt install -y python3 python3-pip
RUN apt-get install -y vim
RUN apt install -y python3-bottle

WORKDIR /app

COPY . .

# Adiciona um volume em /app

VOLUME ["/app"]

EXPOSE 8080

CMD ["python3", "route.py"]
