# webscraper
Webscraper for Exam Databases Advanced

You will want to download the Scraper.py & mongodb.py or clone the github to your terminal

Launch these on the terminal using:

"python3 Scrapery.py"
"python3 mongodb.py "

Note that mongodb.py includes the Redis part of the assignment

Next, download the dockerfiles from this repository., dit zijn jouw images

In your terminal you do: 

"docker pull mongo"
"docker pull redis"

Change images into containers:

"docker run --name Scraper {imageID}"
"docker run --name parser {imageID}"
"docker run -p 27017:27017 --name mongo mongo"
"docker run --name redis redis"

Create network & Add containers:

Create network:

"docker network create {networkName}"

Add containers: 
docker network connect {networkName} {containerName}











