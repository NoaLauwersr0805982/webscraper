MAINTAINER noalauwers1
COPY . . 
RUN apt-get update && apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN git clone https://github.com/NoaLauwersr0805982/webscraper.git
RUN cd webscraper
RUN pip3 install requests
RUN pip3 install beautifulsoup4
RUN pip3 install pandas
RUN pip3 install pymongo
RUN pip3 install redis
RUN pip3 install time
RUN cp "webscraper/Scraper.py"
