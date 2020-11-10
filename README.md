# data-exhaust
Repository to Store [Exhaust Data](https://en.wikipedia.org/wiki/Data_exhaust) from different services

## Installation

Clone the repository

## Setup

For this you will need to install [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).

- Inside the `root` folder, place a `.env` file for the docker-compose file to pick its environment variables from; there is a `.sample_env` to use as reference; simply add some passwords to those missing fields and off you go.

- run `docker-compose build` to build the containers

- Finally run `docker-compose up` - this will run the web server.

## Monitoring

You can find the webserver [here](http://localhost:8000/admin/).
You can also access mongo-express [here](http://localhost:8081)

