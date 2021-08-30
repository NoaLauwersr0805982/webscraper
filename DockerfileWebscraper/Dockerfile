FROM ubuntu:latest AS scraper
COPY . .
# python + packages + git
RUN apt-get update && apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN git clone https://github.com/NoaLauwersr0805982/webscraper.git
RUN cd webscraper
RUN apt-get install python3
RUN pip3 install requests
RUN pip3 install beautifulsoup4
RUN pip3 install pandas
RUN pip3 install pymongo
RUN pip3 install redis
# install redis & mongodb
RUN apt install -y redis-server
RUN redis-server --daemonize yes
RUN apt-get update && apt-get install -y mongodb
RUN mkdir -p /data/db/
RUN chown `id -u` /data/db
RUN mongod --fork --logpath /var/log/mongod.log
# start Scraper.py
RUN cp "webscraper/Scraper.py" .
CMD ["python3", "Scraper.py"]
# start mongodb.py
RUN cp "webscraper/mongodb.py" .
CMD ["python3", "mongodb.py"]
